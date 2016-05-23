# -*- coding: utf-8 -*-
"""
This class is aim to install lamp server(Linux, Apache, Mysql and PHP) into your
local environment.

Usage:
    $ sudo pip install ezhost
    $ ezhost lamp or python3 -m ezhost lamp

Author: Zhe Xiao

Date: 05/20/2016

Contact: zhexiao27@gmail.com
    
Github: https://github.com/zhexiao/ezhost.git
"""
import os
from ezhost.ServerAbstract import ServerAbstract

# fabric libs
from fabric.colors import red, green
from fabric.api import env, prompt, run, sudo, local, put
from fabric.contrib.files import exists
from fabric.state import output

# hide exec command
output['running'] = False

class ServerLamp(ServerAbstract):
    def __init__(self):
        """ choose local environment """
        env.host_string = '127.0.0.1:2222'
        env.user = 'vagrant'
        env.password = 'vagrant'
        env.environment = 'local'

    def install(self):
        self.update_sys()
        self.install_apache()

    def update_sys(self):
        """
        update system package
        """
        if prompt(red(' * Update system package (y/n)?'), default='y') == 'y':
            sudo('apt-get update -y')
            print(green(' * successfully updated your system package'))
            print()

    def install_apache(self):
        """ 
        setup libraries 
        """
        if prompt(red(' * Install apache2 (y/n)?'), default='y') == 'y':
            sudo('apt-get install apache2 -y')
            print(green(' * successfully installed apache2'))
            print()

