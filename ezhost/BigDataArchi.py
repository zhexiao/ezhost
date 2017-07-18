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

        if self.prompt_check("Config kafka"):
            self.kafka_config()

        if self.prompt_check("Autostart kafka"):
            self.kafka_autostart()