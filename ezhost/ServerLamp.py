# -*- coding: utf-8 -*-
"""
This class is aim to install lamp server(Linux, Apache, Mysql and PHP) into your
local environment.

Usage:
    $ sudo pip install ezhost
    $ ezhost -s lamp -H 127.0.0.1:2201 -U vagrant -P vagrant

Author: Zhe Xiao

Date: 05/20/2016

Contact: zhexiao27@gmail.com
    
Github: https://github.com/zhexiao/ezhost.git
"""

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
        pass

    def install(self):
        self.update_sys()
        self.install_apache()
        self.install_mysql()
        self.install_php()

    def update_sys(self):
        if prompt(red(' * Update system package (y/n)?'), default='y') == 'y':
            sudo('apt-get update -y')
            print(green(' * successfully updated your system package'))
            print()

    def install_apache(self):
        if prompt(red(' * Install apache2 (y/n)?'), default='y') == 'y':
            sudo('apt-get install apache2 -y')
            print(green(' * successfully installed apache2'))
            print()

    def install_mysql(self):
        if prompt(red(' * Install mysql (y/n)?'), default='y') == 'y':
            sudo("debconf-set-selections <<< 'mysql-server mysql-server/root_password password {0}'".format(self.mysql_password))
            sudo("debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password {0}'".format(self.mysql_password))
            sudo('apt-get install mysql-server php5-mysql -y')
            print(green(' * successfully installed mysql'))
            print()

    def install_php(self):
        if prompt(red(' * Install php5 (y/n)?'), default='y') == 'y':
            sudo('apt-get install php5 php5-cli libapache2-mod-php5 php5-mcrypt -y')
            # do apache config
            sudo('echo "{0}">/etc/apache2/mods-enabled/dir.conf'.format(self.apache_dir_index))
            # write phpinfo for test 
            sudo('echo "{0}">{1}/info.php'.format(self.phpinfo, self.apache_web_dir))
            print(green(' * successfully installed php5'))
            print()

