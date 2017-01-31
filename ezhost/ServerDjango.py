# -*- coding: utf-8 -*-
"""
Install basic django project

Usage:
    $ -s django or -server django

Author: Zhe Xiao
Github: https://github.com/zhexiao/ezhost.git
"""

from ezhost.ServerCommon import ServerCommon

# fabric libs
from fabric.colors import red, green
from fabric.api import prompt, run, sudo
from fabric.state import output
from fabric.context_managers import cd
from fabric.contrib.files import exists

# hide exec command
output['running'] = False


class ServerDjango(ServerCommon):

    def __init__(self, args):
        self.args = args
        self.project = self.args.project

    def install(self):
        self.update_sys()
        self.install_mysql()
        self.install_virtualenv()
        self.install_packages()
        self.install_project()

    def update_sys(self):
        if self.args.force or prompt(red(' * Update system package (y/n)?'), default='y') == 'y':
            self.common_update_sys()

    def install_mysql(self):
        if self.args.force or prompt(red(' * Install MySql (y/n)?'), default='y') == 'y':
            # python pip mysqlclient dependency
            sudo('apt-get install python3-dev libmysqlclient-dev -y')

            self.common_install_mysql()

    def install_virtualenv(self):
        if self.args.force or prompt(red(' * Install Python3 virtual environment (y/n)?'), default='y') == 'y':
            self.common_install_python_env()

    def install_packages(self):
        if self.args.force or prompt(red(' * Install Python3 packages into virtual environment (y/n)?'), default='y') == 'y':
            # go to virtualenv folder
            with cd(self.python_env_dir):
                run('./bin/pip install django djangorestframework django-filter markdown mysqlclient')
                run('./bin/pip freeze')

                print(green(' * Installed Python3 packages into virtual environment.'))
                print(green(' * Done '))
                print()

    def install_project(self):
        if self.args.force or prompt(red(' * Install Django project at /var/www/html (y/n)?'), default='y') == 'y':
            # check project folder
            if not exists(self.nginx_web_dir):
                sudo('mkdir -p {0}'.format(self.nginx_web_dir))

            # go to project folder and create django project
            with cd(self.nginx_web_dir):
                sudo('{0}/bin/django-admin startproject {1}'.format(self.python_env_dir, self.project))
                sudo('chmod -R 777 {0}/{1}'.format(self.nginx_web_dir, self.project))

            print(green(' * Installed Django project at /var/www/html.'))
            print(green(' * Done '))
            print()
