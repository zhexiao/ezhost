# -*- coding: utf-8 -*-
"""
This class is used for create the common command such as mysql install, nginx install
and so on..

Author: Zhe Xiao
Github: https://github.com/zhexiao/ezhost.git
"""

from io import StringIO

from ezhost.ServerAbstract import ServerAbstract
import ezhost.config.bigdata_conf_string as bigdata_conf

# fabric libs
from fabric.colors import red, green
from fabric.api import prompt, run, sudo, put, env
from fabric.contrib.files import exists, append, comment, sed, uncomment
from fabric.context_managers import cd


class ServerCommon(ServerAbstract):
    """
        All common function will create inside this class.
    """

    def prompt_check(self, message):
        message += ' (y/n)'
        p_signal = prompt(red(message), default='n')
        if p_signal == 'y':
            return True
        return False

    def common_update_sys(self):
        """
            update system package
        """
        try:
            sudo('apt-get update -y')
        except Exception as e:
            print(e)

        print(green('System package is up to date.'))
        print()

    def common_install_mysql(self):
        """
            Install mysql
        """
        sudo("debconf-set-selections <<< 'mysql-server mysql-server/root_password password {0}'".format(self.mysql_password))
        sudo("debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password {0}'".format(self.mysql_password))
        sudo('apt-get install mysql-server -y')

        print(green(' * Installed MySql server in the system.'))
        print(green(' * Done'))
        print()

    def update_source_list(self):
        """
        update ubuntu 16 source list
        :return: 
        """
        with cd('/etc/apt'):
            sudo('mv sources.list sources.list.bak')
            put(StringIO(bigdata_conf.ubuntu_source_list_16),
                'sources.list', use_sudo=True)
            sudo('apt-get update -y')

    def common_install_nginx(self):
        """
            Install nginx
        """
        run('echo "deb http://ppa.launchpad.net/nginx/stable/ubuntu $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/nginx-stable.list')
        sudo('apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C300EE8C')
        sudo('apt-get update -y')
        sudo('apt-get install nginx -y')

        print(green(' * Installed Nginx in the system.'))
        print(green(' * Done'))
        print()

    def common_config_nginx_ssl(self):
        """
            Convert nginx server from http to https
        """
        if prompt(red(' * Change url from http to https (y/n)?'), default='n') == 'y':
            if not exists(self.nginx_ssl_dir):
                sudo('mkdir -p {0}'.format(self.nginx_ssl_dir))

            # generate ssh key
            sudo('openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout {0}/cert.key -out {0}/cert.pem'.format(self.nginx_ssl_dir))

            # do nginx config config
            put(StringIO(self.nginx_web_ssl_config), '/etc/nginx/sites-available/default', use_sudo=True)

            sudo('service nginx restart')

            print(green(' * Make Nginx from http to https.'))
            print(green(' * Done'))
            print()

    def common_install_apache2(self):
        """
            Install apache2 web server
        """
        try:
            sudo('apt-get install apache2 -y')
        except Exception as e:
            print(e)

        print(green(' * Installed Apache2 in the system.'))
        print(green(' * Done'))
        print()

    def common_install_python_env(self):
        """
            Install python virtualenv
        """
        sudo('apt-get install python3 python3-pip -y')
        sudo('pip3 install virtualenv')

        run('virtualenv {0}'.format(self.python_env_dir))

        print(green(' * Installed Python3 virtual environment in the system.'))
        print(green(' * Done'))
        print()

    def systemctl_autostart(self, service_name, start_cmd, stop_cmd):
        """
        ubuntu 16.04 systemctl service config
        :param service_name:
        :param start_cmd:
        :param stop_cmd:
        :return:
        """
        # get config content
        service_content = bigdata_conf.systemctl_config.format(
            service_name=service_name,
            start_cmd=start_cmd,
            stop_cmd=stop_cmd
        )

        # write config into file
        with cd('/lib/systemd/system'):
            if not exists(service_name):
                sudo('touch {0}'.format(service_name))
            put(StringIO(service_content), service_name, use_sudo=True)

        # make service auto-start
        sudo('systemctl daemon-reload')
        sudo('systemctl disable {0}'.format(service_name))
        sudo('systemctl stop {0}'.format(service_name))
        sudo('systemctl enable {0}'.format(service_name))
        sudo('systemctl start {0}'.format(service_name))

    def java_install(self):
        """
        install java
        :return:
        """
        sudo('apt-get install openjdk-8-jdk -y')

        java_home = run('readlink -f /usr/bin/java | '
                        'sed "s:/jre/bin/java::"')

        append(bigdata_conf.global_env_home, 'export JAVA_HOME={0}'.format(
            java_home
        ), use_sudo=True)
        run('source {0}'.format(bigdata_conf.global_env_home))

    def kafka_install(self):
        """
        kafka download and install
        :return:
        """
        with cd('/tmp'):
            if not exists('kafka.tgz'):
                sudo('wget {0} -O kafka.tgz'.format(
                    bigdata_conf.kafka_download_url
                ))

            sudo('tar -zxf kafka.tgz')

            sudo('rm -rf {0}'.format(bigdata_conf.kafka_home))
            sudo('mv kafka_* {0}'.format(bigdata_conf.kafka_home))

    def kafka_config(self):
        """
        kafka config
        :return:
        """
        # 读取配置文件中的端口
        config_obj = self.configure[self.args.config[1]]
        kafka_ports = config_obj.get('KAFKA_PORTS')
        # 默认端口9092
        if not kafka_ports:
            kafka_ports_arr = ['9092']
        else:
            kafka_ports_arr = kafka_ports.replace(' ', '').split(',')

        # chmod project root owner
        sudo('chown {user}:{user} -R {path}'.format(
            user=config_obj.get('user'),
            path=bigdata_conf.project_root
        ))
        # change kafka bin permission for JAVA
        sudo('chmod -R 777 {0}/bin'.format(bigdata_conf.kafka_home))

        # 配置zookeeper服务
        self.systemctl_autostart(
            'zookeeper.service',
            '/opt/kafka/bin/zookeeper-server-start.sh /opt/kafka/config/zookeeper.properties',
            '/opt/kafka/bin/zookeeper-server-stop.sh /opt/kafka/config/zookeeper.properties'
        )

        # 循环生成kafka配置文件
        with cd('{0}/config'.format(bigdata_conf.kafka_home)):
            for idx, k_port in enumerate(kafka_ports_arr):
                conf_file = 'server.properties-{0}'.format(k_port)
                run('cp server.properties {0}'.format(conf_file))

                # 修改kafka配置文件
                sed(conf_file, 'broker.id=.*', 'broker.id={0}'.format(idx))
                uncomment(conf_file, 'listeners=PLAINTEXT')
                sed(conf_file, 'PLAINTEXT://.*', 'PLAINTEXT://{0}:{1}'.format(
                    env.host_string, k_port
                ))
                sed(conf_file, 'log.dirs=.*',
                    'log.dirs=/tmp/kafka-log-{0}'.format(k_port))

                # 配置kafka服务
                self.systemctl_autostart(
                    'kafka-{0}.service'.format(k_port),
                    '/opt/kafka/bin/kafka-server-start.sh /opt/kafka/config/{0}'.format(conf_file),
                    '/opt/kafka/bin/kafka-server-stop.sh /opt/kafka/config/{0}'.format(conf_file)
                )

    def elastic_install(self):
        """
        elasticsearch install
        :return:
        """
        with cd('/tmp'):
            if not exists('elastic.deb'):
                sudo('wget {0} -O elastic.deb'.format(
                    bigdata_conf.elastic_download_url
                ))

            sudo('dpkg -i elastic.deb')
            sudo('apt-get install -y')

    def elastic_config(self):
        """
        config elasticsearch
        :return:
        """
        sudo('systemctl stop elasticsearch.service')
        sudo('systemctl daemon-reload')
        sudo('systemctl enable elasticsearch.service')
        sudo('systemctl start elasticsearch.service')

    def logstash_install(self):
        """
        logstash install
        :return:
        """
        with cd('/tmp'):
            if not exists('logstash.deb'):
                sudo('wget {0} -O logstash.deb'.format(
                    bigdata_conf.logstash_download_url
                ))

            sudo('dpkg -i logstash.deb')
            sudo('apt-get install -y')

    def logstash_config(self):
        """
        config logstash
        :return:
        """
        sudo('systemctl stop logstash.service')
        sudo('systemctl daemon-reload')
        sudo('systemctl enable logstash.service')
        sudo('systemctl start logstash.service')

    def kibana_install(self):
        """
        kibana install
        :return:
        """
        with cd('/tmp'):
            if not exists('kibana.deb'):
                sudo('wget {0} -O kibana.deb'.format(
                    bigdata_conf.kibana_download_url
                ))

            sudo('dpkg -i kibana.deb')
            sudo('apt-get install -y')

    def kibana_config(self):
        """
        config kibana
        :return:
        """

        uncomment("/etc/kibana/kibana.yml", "#server.host:", use_sudo=True)
        sed('/etc/kibana/kibana.yml', 'server.host:.*',
            'server.host: "{0}"'.format(env.host_string), use_sudo=True)
        sudo('systemctl stop kibana.service')
        sudo('systemctl daemon-reload')
        sudo('systemctl enable kibana.service')
        sudo('systemctl start kibana.service')

    def hadoop_install(self):
        """
        install hadoop
        :return:
        """
        with cd('/tmp'):
            if not exists('hadoop.tar.gz'):
                sudo('wget {0} -O hadoop.tar.gz'.format(
                    bigdata_conf.hadoop_download_url
                ))

            sudo('rm -rf hadoop-*')
            sudo('tar -zxf hadoop.tar.gz')
            sudo('rm -rf {0}'.format(bigdata_conf.hadoop_home))
            sudo('mv hadoop-* {0}'.format(bigdata_conf.hadoop_home))

    def spark_install(self):
        """
        download and install spark
        :return:
        """
        sudo('apt-get -y install build-essential python-dev python-six \
             python-virtualenv libcurl4-nss-dev libsasl2-dev libsasl2-modules \
             maven libapr1-dev libsvn-dev zlib1g-dev')

        with cd('/tmp'):
            if not exists('spark.tgz'):
                sudo('wget {0} -O spark.tgz'.format(
                    bigdata_conf.spark_download_url
                ))

            sudo('rm -rf spark-*')
            sudo('tar -zxf spark.tgz')
            sudo('rm -rf {0}'.format(bigdata_conf.spark_home))
            sudo('mv spark-* {0}'.format(bigdata_conf.spark_home))

    def spark_config(self):
        """
        config spark
        :return:
        """
        configs = [
            'export LD_LIBRARY_PATH={0}/lib/native/:$LD_LIBRARY_PATH'.format(
                bigdata_conf.hadoop_home
            ),
            'export SPARK_LOCAL_IP={0}'.format(env.host_string)
        ]

        append(bigdata_conf.global_env_home, configs, use_sudo=True)
        run('source {0}'.format(bigdata_conf.global_env_home))

    def reset_server_env(self, server_name, configure):
        """
        reset server env to server-name
        :param server_name:
        :param configure:
        :return:
        """
        env.host_string = configure[server_name]['host']
        env.user = configure[server_name]['user']
        env.password = configure[server_name]['passwd']

    def generate_ssh(self, server, args, configure):
        """
        异步同时执行SSH生成 generate ssh
        :param server:
        :param args:
        :param configure:
        :return:
        """
        self.reset_server_env(server, configure)

        # chmod project root owner
        sudo('chown {user}:{user} -R {path}'.format(
            user=configure[server]['user'],
            path=bigdata_conf.project_root
        ))

        # generate ssh key
        if not exists('~/.ssh/id_rsa.pub'):
            run('ssh-keygen -t rsa -P "" -f ~/.ssh/id_rsa')

    def add_spark_slave(self, master, slave, configure):
        """
        add spark slave
        :return:
        """
        # go to master server, add config
        self.reset_server_env(master, configure)
        with cd(bigdata_conf.spark_home):
            if not exists('conf/spark-env.sh'):
                sudo('cp conf/spark-env.sh.template conf/spark-env.sh')

            spark_env = bigdata_conf.spark_env.format(
                spark_home=bigdata_conf.spark_home,
                hadoop_home=bigdata_conf.hadoop_home,
                host=env.host_string,
                SPARK_WORKER_MEMORY=configure[master].get(
                    'SPARK_WORKER_MEMORY', '512M'
                )
            )

            put(StringIO(spark_env), 'conf/spark-env.sh', use_sudo=True)

            if not exists('conf/slaves'):
                sudo('cp conf/slaves.template conf/slaves')

        # comment slaves localhost
        comment('{0}/conf/slaves'.format(bigdata_conf.spark_home),
                'localhost', use_sudo=True)

        # add slave into config
        append('{0}/conf/slaves'.format(bigdata_conf.spark_home),
               '\n{0}'.format(configure[slave]['host']), use_sudo=True)

        run('scp -r {0} {1}@{2}:/opt'.format(
            bigdata_conf.spark_home,
            configure[slave]['user'],
            configure[slave]['host']
        ))

        # go to slave server
        self.reset_server_env(slave, configure)

        append(bigdata_conf.global_env_home, 'export SPARK_LOCAL_IP={0}'.format(
            configure[slave]['host']
        ), use_sudo=True)
        run('source {0}'.format(bigdata_conf.global_env_home))

        # go to master server, restart server
        self.reset_server_env(master, configure)
        with cd(bigdata_conf.spark_home):
            run('./sbin/stop-master.sh')
            run('./sbin/stop-slaves.sh')
            run('./sbin/start-master.sh')
            run('./sbin/start-slaves.sh')

