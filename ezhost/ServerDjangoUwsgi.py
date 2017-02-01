# -*- coding: utf-8 -*-
"""
This class is aim to install Django Applications with uWSGI and Nginx,
we will using linux supervisor to control the server auto start.

Usage:
    $ sudo pip install ezhost
    $ ezhost -s django-uwsgi -H 127.0.0.1:2200 -U vagrant -P vagrant

Author: Zhe Xiao
Github: https://github.com/zhexiao/ezhost.git
"""

from io import StringIO

# fabric libs
from fabric.colors import red, green
from fabric.api import prompt, run, sudo, put
from fabric.contrib.files import exists
from fabric.state import output
from fabric.context_managers import cd

from ezhost.ServerCommon import ServerCommon
from ezhost.ServerDjango import ServerDjango

# hide exec command
output['running'] = False


class ServerDjangoUwsgi(ServerCommon):
    def __init__(self, args):
        self.args = args
        self.project = self.args.project
        self.project_dir = '{0}/{1}'.format(self.nginx_web_dir, self.project)

    def install(self):
        # install basic django server
        ServerDjango(self.args).install()

        self.install_nginx()
        self.install_uwsgi()
        self.install_supervisor()

    def install_nginx(self):
        if self.args.force or prompt(red(' * Install Nginx (y/n)?'), default='y') == 'y':
            self.common_install_nginx()

            # nginx configuration
            put(StringIO(self.django_uwsgi_with_nginx), '/etc/nginx/sites-enabled/default', use_sudo=True)

            # restart server
            sudo('service nginx restart')

    def install_uwsgi(self):
        if self.args.force or prompt(red(' * Install Uwsgi service (y/n)?'), default='y') == 'y':
            sudo('pip3 install uwsgi')

            # uwsgi config need real env path
            with cd(self.python_env_dir):
                real_env_path = run('pwd')

            # get user
            home_user = run('echo $USER')

            # uwsgi config string
            django_uwsgi_ini = self.django_uwsgi_ini.format(self.nginx_web_dir, self.project, real_env_path, home_user)

            # modify uwsgi config file
            with cd(self.project_dir):
                if not exists('{0}.ini'.format(self.project)):
                    run('touch {0}.ini'.format(self.project))

                put(StringIO(django_uwsgi_ini), '{0}.ini'.format(self.project), use_sudo=True)

            print(green(' * Installed Uwsgi service in the system.'))
            print(green(' * Done '))
            print()

    def install_supervisor(self):
        if self.args.force or prompt(red(' * Install Supervisor controller for Uwsgi (y/n)?'), default='y') == 'y':
            sudo('apt-get install supervisor -y')

            # supervisor config string
            supervisor_uwsgi_ini = self.supervisor_uwsgi_ini.format(self.project, self.project_dir)

            # create supervisor control configruation
            with cd(self.supervisor_config_dir):
                if not exists('{0}_sysd.conf'.format(self.project)):
                    sudo('touch {0}_sysd.conf'.format(self.project))

                # supervisor control uwsgi config
                put(StringIO(supervisor_uwsgi_ini), '{0}_sysd.conf'.format(self.project), use_sudo=True)

            # create supervisor log and error file
            with cd('/var/log'):
                if not exists('{0}_out.log'.format(self.project)):
                    sudo('touch {0}_out.log'.format(self.project))

                if not exists('{0}_error.log'.format(self.project)):
                    sudo('touch {0}_error.log'.format(self.project))

            # enable and start supervisor
            try:
                # ubuntu 16
                sudo('systemctl enable supervisor')
                sudo('systemctl start supervisor')
            except:
                # ubuntu 14
                sudo('supervisorctl reread')
                sudo('supervisorctl update')
                sudo('update-rc.d supervisor enable')

            print(green(' * Installed Supervisor controller in the system.'))
            print(green(' * Done '))
            print()
