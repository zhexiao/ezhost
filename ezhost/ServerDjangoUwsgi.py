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

from io import StringIO

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
        self.project = self.args.project
        self.project_dir = '{0}/{1}'.format(self.nginx_web_dir, self.project)

    def install(self):
        self.update_sys()
        self.install_mysql()
        self.install_libraries()
        self.install_project()
        self.install_nginx()
        self.install_uwsgi()
        self.install_supervisor()

    def update_sys(self):
        if self.args.force or prompt(red(' * Update system package (y/n)?'), default='y') == 'y':
            sudo('apt-get update -y')

            print(green(' * successfully updated your system package'))
            print()

    def install_mysql(self):
        if self.args.force or prompt(red(' * Install mysql (y/n)?'), default='y') == 'y':
            sudo("debconf-set-selections <<< 'mysql-server mysql-server/root_password password {0}'".format(self.mysql_password))
            sudo("debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password {0}'".format(self.mysql_password))
            sudo('apt-get install mysql-server -y')

            print(green(' * Done'))
            print()

    def install_libraries(self):
        if self.args.force or prompt(red(' * Install libraries (y/n)?'), default='y') == 'y':
            sudo('apt-get install python3 python3-pip python-pip -y')
            sudo('pip install virtualenv')

            print(green(' * Done '))
            print()

    def install_project(self):
        if self.args.force or prompt(red(' * Install Django project (y/n)?'), default='y') == 'y':
            # create project
            if not exists( self.project_dir ):
                sudo('mkdir -p {0}'.format(self.project_dir) )
            sudo('chmod -R 777 {0}'.format(self.project_dir) )

            # create project virtualenv
            run('virtualenv -p python3 {0}'.format(self.python_env_dir) )
            run('{0}/bin/pip install django markdown django-filter'.format(self.python_env_dir) )
            run('cd {0} && {1}/bin/django-admin startproject {2} .'.format(self.project_dir, self.python_env_dir, self.project))

            print(green(' * Done '))
            print()

    def install_nginx(self):
        if self.args.force or prompt(red(' * Install Nginx server (y/n)?'), default='y') == 'y':
            sudo('apt-get install nginx -y')

            # nginx configuration
            put(StringIO(self.django_uwsgi_with_nginx), '/etc/nginx/sites-enabled/default', use_sudo=True)

            # restart server and supervisor
            sudo('service nginx restart')

            print(green(' * Done '))
            print()

    def install_uwsgi(self):
        if self.args.force or prompt(red(' * Install Uwsgi service (y/n)?'), default='y') == 'y':
            sudo('pip3 install uwsgi')
            
            # create uwsgi ini file
            if not exists('{0}/{1}.ini'.format(self.project_dir, self.project)):
                run('touch {0}/{1}.ini'.format(self.project_dir, self.project))

            # uwsgi configuration
            django_uwsgi_ini = self.django_uwsgi_ini.format(self.nginx_web_dir, self.project, self.python_env_dir)
            put(StringIO(django_uwsgi_ini), '{0}/{1}.ini'.format(self.project_dir, self.project), use_sudo=True)

            print(green(' * Done '))
            print()

    def install_supervisor(self):
        if self.args.force or prompt(red(' * Install Supervisor for control Uwsgi service (y/n)?'), default='y') == 'y':
            sudo('apt-get install supervisor -y')

            # create supervisor control configruation
            if not exists('{0}/{1}_sysd.conf'.format(self.supervisor_config_dir, self.project) ):
                sudo('touch {0}/{1}_sysd.conf'.format(self.supervisor_config_dir, self.project) )

            # create supervisor log and error file
            if not exists('/var/log/{0}_out.log'.format(self.project) ):
                sudo('touch /var/log/{0}_out.log'.format(self.project) )
            if not exists('/var/log/{0}_error.log'.format(self.project) ):
                sudo('touch /var/log/{0}_error.log'.format(self.project) )

            # supervisor control uwsgi config
            supervisor_uwsgi_ini = self.supervisor_uwsgi_ini.format(self.project, self.project_dir)
            put(StringIO(supervisor_uwsgi_ini), '{0}/{1}_sysd.conf'.format(self.supervisor_config_dir, self.project) , use_sudo=True)

            sudo('sudo supervisorctl reread && sudo supervisorctl update')

            print(green(' * Done '))
            print()