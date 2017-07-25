# -*- coding: utf-8 -*-
"""
BigData Architecture Class

Author: Zhe Xiao
Github: https://github.com/zhexiao/ezhost.git
"""
from ezhost.ServerCommon import ServerCommon

# fabric libs
from fabric.state import output
from fabric.api import run, sudo


# hide exec command
output['running'] = False


class BigDataArchi(ServerCommon):

    def __init__(self, args, **kwargs):
        self.args = args
        self.configure = kwargs.get('configure')

        if self.args.bigdata_app is None:
            raise Exception('请使用`-ba`指定需要安装的应用')

    def install(self):
        if not self.args.skip_master:
            # update source list
            if self.prompt_check("Change ubuntu 16 source lists"):
                self.update_source_list()

            # update package
            if self.prompt_check("Update system package"):
                self.common_update_sys()

            # JAVA
            if self.prompt_check("Install Java JDK"):
                self.java_install()

            # check bigdata app
            if self.args.bigdata_app == 'kafka':
                self.install_config_kafka()
            elif self.args.bigdata_app == 'elastic':
                self.install_config_elastic()
            elif self.args.bigdata_app == 'logstash':
                self.install_config_logstash()
            elif self.args.bigdata_app == 'kibana':
                self.install_config_kibana()
            elif self.args.bigdata_app == 'elk':
                self.install_config_elk()
            elif self.args.bigdata_app == 'spark':
                self.install_config_spark()
            else:
                raise Exception('找不到匹配的应用')

        if self.args.add_slave is not None:
            self.add_slave_server()

    def install_config_kafka(self):
        """
        install and config kafka
        :return:
        """
        if self.prompt_check("Download and install kafka"):
            self.kafka_install()

        if self.prompt_check("Configure and autostart kafka"):
            self.kafka_config()

    def install_config_elastic(self):
        """
        install and config elasticsearch
        :return:
        """
        if self.prompt_check("Download and install elasticsearch"):
            self.elastic_install()

        if self.prompt_check("Configure and autostart elasticsearch"):
            self.elastic_config()

    def install_config_logstash(self):
        """
        install and config logstash
        :return:
        """
        if self.prompt_check("Download and install logstash"):
            self.logstash_install()

        if self.prompt_check("Configure and autostart logstash"):
            self.logstash_config()

    def install_config_kibana(self):
        """
        install and config kibana
        :return:
        """
        if self.prompt_check("Download and install kibana"):
            self.kibana_install()

        if self.prompt_check("Configure and autostart kibana"):
            self.kibana_config()

    def install_config_elk(self):
        """
        install and config elk
        :return:
        """
        self.install_config_elastic()
        self.install_config_kibana()
        self.install_config_logstash()

    def install_config_spark(self):
        """
        install and config spark
        :return:
        """
        if self.prompt_check("Download and install hadoop"):
            self.hadoop_install()

        if self.prompt_check("Download and install spark"):
            self.spark_install()

        if self.prompt_check("Configure spark"):
            self.spark_config()

    def add_slave_server(self):
        """
        添加slave服务器
        :return:
        """
        master = self.args.config[1]
        slave = self.args.add_slave

        # install java at slave server
        self.reset_server_env(slave, self.configure)
        if self.prompt_check("Update package at slave server"):
            self.common_update_sys()

        if self.prompt_check("Install java and python at slave server"):
            self.java_install()
            sudo('apt-get install -y python python3 python-dev python3-dev')

        # generate ssh key at master server
        if not self.args.skip_master:
            if self.prompt_check("Generate ssh key at Master Server"):
                self.generate_ssh(master, self.args, self.configure)

        # generate ssh key at slave server and make slave connect with master
        if self.prompt_check("Make ssh connection within master and slave"):
            self.generate_ssh(slave, self.args, self.configure)

            # scp slave server ssh key to master server
            run('scp ~/.ssh/id_rsa.pub {0}@{1}:~/.ssh/id_rsa.pub.{2}'.format(
                self.configure[master]['user'],
                self.configure[master]['host'],
                slave
            ))

            # add slave ssh key to master authorized_keys
            self.reset_server_env(master, self.configure)
            run('cat ~/.ssh/id_rsa.pub* >> ~/.ssh/authorized_keys')

            # scp master authorized_keys to slave authorized_keys
            run('scp ~/.ssh/authorized_keys {0}@{1}:~/.ssh'.format(
                self.configure[slave]['user'],
                self.configure[slave]['host']
            ))

        # config slave and master
        if self.prompt_check("Configure master and slave server"):
            master = self.args.config[1]
            slave = self.args.add_slave

            if self.args.bigdata_app == 'spark':
                self.add_spark_slave(master, slave, self.configure)



