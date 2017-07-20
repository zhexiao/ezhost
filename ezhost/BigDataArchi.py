# -*- coding: utf-8 -*-
"""
BigData Architecture Class

Author: Zhe Xiao
Github: https://github.com/zhexiao/ezhost.git
"""
from ezhost.ServerCommon import ServerCommon
import ezhost.config.bigdata_conf_string as bigdata_conf

# fabric libs
from fabric.colors import red, green
from fabric.api import sudo
from fabric.state import output
from fabric.context_managers import cd

# hide exec command
output['running'] = False


class BigDataArchi(ServerCommon):

    def __init__(self, args):
        self.args = args
        if self.args.bigdata_app is None:
            raise Exception('请使用`-ba`指定需要安装的应用')

    def install(self):
        self.update_sys()
        self.java_install()
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
        else:
            raise Exception('找不到匹配的应用')

    def update_sys(self):
        if self.prompt_check("Update system package"):
            self.common_update_sys()

    def install_config_kafka(self):
        """
        install and config kafka
        :return:
        """
        if self.prompt_check("Download and install kafka"):
            self.kafka_install()

        if self.prompt_check("Config and autostart kafka"):
            self.kafka_config()

    def install_config_elastic(self):
        """
        install and config elasticsearch
        :return:
        """
        if self.prompt_check("Download and install elasticsearch"):
            self.elastic_install()

        if self.prompt_check("Config and autostart elasticsearch"):
            self.elastic_config()

    def install_config_logstash(self):
        """
        install and config logstash
        :return:
        """
        if self.prompt_check("Download and install logstash"):
            self.logstash_install()

        if self.prompt_check("Config and autostart logstash"):
            self.logstash_config()

    def install_config_kibana(self):
        """
        install and config kibana
        :return:
        """
        if self.prompt_check("Download and install kibana"):
            self.kibana_install()

        if self.prompt_check("Config and autostart kibana"):
            self.kibana_config()

    def install_config_elk(self):
        """
        install and config elk
        :return:
        """
        self.install_config_elastic()
        self.install_config_kibana()
        self.install_config_logstash()