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
from fabric.api import prompt, run, sudo, put
from fabric.contrib.files import exists
from fabric.context_managers import cd
from fabric.api import env
from fabric.contrib.files import sed, uncomment


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
        sudo('systemctl enable {0}'.format(service_name))
        sudo('systemctl start {0}'.format(service_name))

    def java_install(self):
        """
        install java
        :return:
        """
        if self.prompt_check("Install Java JDK"):
            sudo('apt-get install default-jdk -y')

    def kafka_install(self):
        """
        kafka download and install
        :return:
        """
        with cd('/tmp'):
            sudo('rm -rf kafka*')
            sudo('wget {0} -O kafka.tgz'.format(
                bigdata_conf.kafka_download_url
            ))

            sudo('tar -zxf kafka.tgz')

            if not exists(bigdata_conf.kafka_home):
                sudo('mv kafka_* {0}'.format(bigdata_conf.kafka_home))

            print(green('Install kafka at {0}'.format(
                bigdata_conf.kafka_home
            )))
            print()

    def kafka_config(self):
        """
        kafka config
        :return:
        """
        uncomment('{0}/config/server.properties'.format(bigdata_conf.kafka_home)
                  , 'delete.topic.enable=true', use_sudo=True)
        uncomment('{0}/config/server.properties'.format(bigdata_conf.kafka_home)
                  , 'listeners=PLAINTEXT', use_sudo=True)
        sed('{0}/config/server.properties'.format(bigdata_conf.kafka_home),
            'PLAINTEXT://.*', 'PLAINTEXT://{0}:9092'.format(env.host_string),
            use_sudo=True)

        self.systemctl_autostart(
            'ez_kafka_zookeeper.service',
            '/opt/kafka/bin/zookeeper-server-start.sh /opt/kafka/config/zookeeper.properties',
            '/opt/kafka/bin/zookeeper-server-stop.sh /opt/kafka/config/zookeeper.properties'
        )

        self.systemctl_autostart(
            'ez_kafka.service',
            '/opt/kafka/bin/kafka-server-start.sh /opt/kafka/config/server.properties',
            '/opt/kafka/bin/kafka-server-stop.sh /opt/kafka/config/server.properties'
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
        sudo('systemctl stop kibana.service')
        sudo('systemctl daemon-reload')
        sudo('systemctl enable kibana.service')
        sudo('systemctl start kibana.service')

    def elk_install(self):
        """
        elastic, logstash, kibana install
        :return:
        """
        self.elastic_install()
        self.logstash_install()
        self.kibana_install()

    def elk_config(self):
        """
        elastic, logstash, kibana config
        :return:
        """
        self.elastic_config()
        self.logstash_config()
        self.kibana_config()