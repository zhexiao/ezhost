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
        if prompt(red(' * Update system package (y/n)?'), default='y') == 'y':
            sudo('apt-get update -y')
            print(green(' * successfully updated your system package'))
            print()

    def install_mysql(self):
        if prompt(red(' * Install mysql (y/n)?'), default='y') == 'y':
            sudo("debconf-set-selections <<< 'mysql-server mysql-server/root_password password {0}'".format(self.mysql_password))
            sudo("debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password {0}'".format(self.mysql_password))
            sudo('apt-get install mysql-server php5-mysql -y')
            print(green(' * successfully installed Mysql'))
            print()

    def install_nginx(self):
        if prompt(red(' * Install Nginx (y/n)?'), default='y') == 'y':
            run('echo "deb http://ppa.launchpad.net/nginx/stable/ubuntu $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/nginx-stable.list')
            sudo('apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C300EE8C')
            sudo('apt-get update -y')
            sudo('apt-get install nginx -y')
            print(green(' * successfully installed Nginx'))
            print()


    def install_php(self):
        if prompt(red(' * Install php5 (y/n)?'), default='y') == 'y':
            # Find the line, cgi.fix_pathinfo=1, and change the 1 to 0.
            sudo('apt-get install php5-fpm -y')
            sed('/etc/php5/fpm/php.ini', ';cgi.fix_pathinfo=1', 'cgi.fix_pathinfo=0', use_sudo=True)

            # do nginx config config
            sudo('echo "{0}">/etc/nginx/sites-available/default'.format(self.nginx_web_config))
            # write phpinfo for test 
            sudo('echo "{0}">{1}/info.php'.format(self.phpinfo, self.nginx_web_dir))

            sudo('service php5-fpm restart')
            sudo('service nginx restart')
            print(green(' * successfully installed php5'))
            print()

