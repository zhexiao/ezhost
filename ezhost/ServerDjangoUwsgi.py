# -*- coding: utf-8 -*-
"""
This class is aim to install Django Applications with uWSGI and Nginx, 
we will using linux supervisor to control the server auto start.

Usage:
    $ sudo pip install ezhost
    $ ezhost -s django-uwsgi -H 127.0.0.1:2200 -U vagrant -P vagrant

Author: Zhe Xiao

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

class ServerDjangoUwsgi(ServerAbstract):
    def __init__(self, args):
        self.args = args

    def install(self):
        self.update_sys()
        self.install_libraries()
        self.install_project()
        self.install_uwsgi()

    def update_sys(self):
        if prompt(red(' * Update system package (y/n)?'), default='y') == 'y':
            sudo('apt-get update -y')
            print(green(' * successfully updated your system package'))
            print()

    def install_libraries(self):
        if prompt(red(' * Install libraries (y/n)?'), default='y') == 'y':
            sudo("apt-get install python3 python3-dev python3-pip python3.4-venv -y")
            sudo("apt-get install python-mysqldb -y")
            print(green(' * Done '))
            print()
        # mysql
        # sudo("debconf-set-selections <<< 'mysql-server mysql-server/root_password password {0}'".format(self.mysql_password))
        # sudo("debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password {0}'".format(self.mysql_password))
        # sudo('apt-get install mysql-server -y')
        # uwsgi
        # sudo('pip3 install uwsgi')
        # 
    def install_project(self):
        if prompt(red(' * Install Django project (y/n)?'), default='y') == 'y':
            # create project virtualenv
            if not exists(self.python_env_dir):
                run('mkdir {0}'.format(self.python_env_dir))
            run('python3 -m venv {0}/{1}'.format(self.python_env_dir, self.args.project))
            run("{0}/{1}/bin/pip install django".format(self.python_env_dir, self.args.project))

            # create project
            if not exists(self.nginx_web_dir):
                sudo('mkdir -p {0}'.format(self.nginx_web_dir))
            sudo('chmod -R 777 {0}'.format(self.nginx_web_dir))
            run('cd {0} && {1}/{2}/bin/django-admin startproject {1}'.format(self.nginx_web_dir, self.python_env_dir, self.args.project))
            print(green(' * Done '))
            print()

    def install_uwsgi(self):
        if prompt(red(' * Install Uwsgi with Nginx (y/n)?'), default='y') == 'y':
            sudo('apt-get install nginx -y')
            sudo('{0}/{1}/bin/pip install uwsgi'.format(self.python_env_dir, self.args.project))
            print(green(' * Done '))
            print()