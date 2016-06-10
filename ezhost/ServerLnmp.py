# -*- coding: utf-8 -*-
"""
This class is aim to install lnmp server(Linux, Nginx, Mysql and PHP) into your
local environment.

Usage:
    $ sudo pip install ezhost
    $ ezhost -s lnmp -H 127.0.0.1:2201 -U vagrant -P vagrant

Author: Zhe Xiao

Contact: zhexiao27@gmail.com
    
Github: https://github.com/zhexiao/ezhost.git
"""

from io import StringIO

from ezhost.ServerAbstract import ServerAbstract

# fabric libs
from fabric.colors import red, green
from fabric.api import env, prompt, run, sudo, local, put
from fabric.contrib.files import exists, sed
from fabric.state import output

# hide exec command
output['running'] = False

class ServerLnmp(ServerAbstract):
    def __init__(self, args):
        self.args = args

    def install(self):
        self.update_sys()
        self.install_mysql()
        self.install_nginx()
        self.install_php()

    def update_sys(self):
        if self.args.force or prompt(red(' * Update system package (y/n)?'), default='y') == 'y':
            sudo('apt-get update -y')

            print(green(' * Done'))
            print()

    def install_mysql(self):
        if self.args.force or prompt(red(' * Install mysql (y/n)?'), default='y') == 'y':
            sudo("debconf-set-selections <<< 'mysql-server mysql-server/root_password password {0}'".format(self.mysql_password))
            sudo("debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password {0}'".format(self.mysql_password))
            sudo('apt-get install mysql-server php5-mysql -y')

            print(green(' * Done'))
            print()

    def install_nginx(self):
        if self.args.force or prompt(red(' * Install Nginx (y/n)?'), default='y') == 'y':
            run('echo "deb http://ppa.launchpad.net/nginx/stable/ubuntu $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/nginx-stable.list')
            sudo('apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C300EE8C')
            sudo('apt-get update -y')
            sudo('apt-get install nginx -y')

            # do nginx config 
            put(StringIO(self.nginx_web_config), '/etc/nginx/sites-available/default', use_sudo=True)


        # want to using https?
        if prompt(red(' * Change url from http to https (y/n)?'), default='y') == 'y':
            if not exists(self.nginx_ssl_dir):
                sudo('mkdir -p {0}'.format(self.nginx_ssl_dir) )
            # generate ssh key
            sudo('openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout {0}/cert.key -out {0}/cert.pem'.format(self.nginx_ssl_dir) )

            # do nginx config config
            put(StringIO(self.nginx_web_ssl_config), '/etc/nginx/sites-available/default', use_sudo=True)

        sudo('service nginx restart')

        print(green(' * Done'))
        print()


    def install_php(self):
        if self.args.force or prompt(red(' * Install php5 (y/n)?'), default='y') == 'y':
            # Find the line, cgi.fix_pathinfo=1, and change the 1 to 0.
            sudo('apt-get install php5-fpm -y')
            sed('/etc/php5/fpm/php.ini', ';cgi.fix_pathinfo=1', 'cgi.fix_pathinfo=0', use_sudo=True)

            # write phpinfo for test 
            put(StringIO(self.phpinfo), '{0}/info.php'.format(self.nginx_web_dir), use_sudo=True)

            sudo('service php5-fpm restart')

            print(green(' * Done'))
            print()

