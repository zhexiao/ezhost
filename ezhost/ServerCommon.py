# -*- coding: utf-8 -*-
"""
This class is used for create the common command such as mysql install, nginx install
and so on..

Author: Zhe Xiao
Github: https://github.com/zhexiao/ezhost.git
"""

from io import StringIO

from ezhost.ServerAbstract import ServerAbstract

# fabric libs
from fabric.colors import red, green
from fabric.api import prompt, run, sudo, put
from fabric.contrib.files import exists


class ServerCommon(ServerAbstract):
    """
        All common function will create inside this class.
    """

    def common_update_sys(self):
        """
            update system package
        """
        sudo('apt-get update -y')

        print(green(' * System package is up to date.'))
        print(green(' * Done'))
        print()

    def common_install_mysql(self):
        """
            Install mysql
        """
        sudo("debconf-set-selections <<< 'mysql-server mysql-server/root_password password {0}'".format(self.mysql_password))
        sudo("debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password {0}'".format(self.mysql_password))
        sudo('apt-get install mysql-server -y')

        print(green(' * Installed MySql server in the system.'))
        print(green(' * Done'))
        print()

    def common_install_nginx(self):
        """
            Install nginx
        """
        run('echo "deb http://ppa.launchpad.net/nginx/stable/ubuntu $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/nginx-stable.list')
        sudo('apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C300EE8C')
        sudo('apt-get update -y')
        sudo('apt-get install nginx -y')

        print(green(' * Installed Nginx in the system.'))
        print(green(' * Done'))
        print()

    def common_config_nginx_ssl(self):
        """
            Convert nginx server from http to https
        """
        if prompt(red(' * Change url from http to https (y/n)?'), default='n') == 'y':
            if not exists(self.nginx_ssl_dir):
                sudo('mkdir -p {0}'.format(self.nginx_ssl_dir))

            # generate ssh key
            sudo('openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout {0}/cert.key -out {0}/cert.pem'.format(self.nginx_ssl_dir))

            # do nginx config config
            put(StringIO(self.nginx_web_ssl_config), '/etc/nginx/sites-available/default', use_sudo=True)

            sudo('service nginx restart')

            print(green(' * Make Nginx from http to https.'))
            print(green(' * Done'))
            print()

    def common_install_apache2(self):
        """
            Install apache2 web server
        """
        sudo('apt-get install apache2 -y')

        print(green(' * Installed Apache2 in the system.'))
        print(green(' * Done'))
        print()

    def common_install_python_env(self):
        """
            Install python virtualenv
        """
        sudo('apt-get install python3 python3-pip -y')
        sudo('pip3 install virtualenv')

        run('virtualenv {0}'.format(self.python_env_dir))

        print(green(' * Installed Python3 virtual environment in the system.'))
        print(green(' * Done'))
        print()
