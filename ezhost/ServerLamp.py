# -*- coding: utf-8 -*-
"""
This class is aim to install lamp server(Linux, Apache, Mysql and PHP) into your
local environment.

Usage:
    $ sudo pip install ezhost
    $ python3 ezhost lamp

Author: Zhe Xiao

Date: 05/20/2016

Contact: zhexiao27@gmail.com
    
Github: https://github.com/zhexiao/ezhost.git
"""

from ServerAbstract import *
import os

class ServerLamp(ServerAbstract):
    def install(self):
        command = 'fab -f /var/www/html/ezhost/ezhost/ServerLamp local setup'
        os.system(command)


def setup():
    """ deploy function """
    if env.environment not in ["local"]:
        print( red(' * please choose a environment.') )
    else:
        # exec the specify environment install function 
        globals()['setup_{0}'.format(env.environment)]()  
        

def local():
    """ choose local environment """
    env.hosts = ['127.0.0.1:2222']
    env.user = 'vagrant'
    env.password = 'vagrant'
    env.environment = 'local'

def setup_local():
    update_sys()
    install_apache()

def update_sys():
    """update system package"""
    sudo('apt-get update -y')
    print(green(' * successfully updated your system package'))

def install_apache():
    """ setup libraries """
    if prompt(red(' * Install apache2 (y/n)?'), default='y') == 'y':
        sudo('apt-get install apache2 -y')
        print(green(' * successfully installed apache2'))

