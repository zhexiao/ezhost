# -*- coding: utf-8 -*-
"""
This class is aim to install lnmp server(Linux, Nginx, Mysql and PHP) into your
local environment.

Usage:
    $ sudo pip install ezhost
    $ ezhost -s lnmp -H 127.0.0.1:2201 -U vagrant -P vagrant

Author: Zhe Xiao
Github: https://github.com/zhexiao/ezhost.git
"""

from io import StringIO

from ezhost.ServerCommon import ServerCommon

# fabric libs
from fabric.colors import red, green
from fabric.api import prompt, sudo, put
from fabric.contrib.files import sed
from fabric.state import output

# hide exec command
output['running'] = False


class ServerLnmp(ServerCommon):

    def __init__(self, args):
        self.args = args

    def install(self):
        self.update_sys()
        self.install_mysql()
        self.install_nginx()
        self.install_php()

    def update_sys(self):
        if self.args.force or prompt(red(' * Update system package (y/n)?'), default='y') == 'y':
            self.common_update_sys()

    def install_mysql(self):
        if self.args.force or prompt(red(' * Install MySql (y/n)?'), default='y') == 'y':
            self.common_install_mysql()

    def install_nginx(self):
        if self.args.force or prompt(red(' * Install Nginx (y/n)?'), default='y') == 'y':
            self.common_install_nginx()

    def install_php(self):
        if self.args.force or prompt(red(' * Install PHP (y/n)?'), default='y') == 'y':
            # try install php7 or php5
            try:
                sudo('apt-get install php7.0-fpm php7.0-mysql php7.0-gd php7.0-curl -y')

                # Find the line, cgi.fix_pathinfo=1, and change the 1 to 0.
                sed('/etc/php/7.0/fpm/php.ini', ';cgi.fix_pathinfo=1', 'cgi.fix_pathinfo=0', use_sudo=True)
                # do nginx config
                put(StringIO(self.nginx_php7_web_config), '/etc/nginx/sites-available/default', use_sudo=True)

                sudo('service nginx restart')
                sudo('service php7.0-fpm restart')
                print(green(' * Installed php7.0 and php7-mysql in the system.'))
            except:
                sudo('apt-get install php5-fpm php5-mysql php5-gd php5-curl -y')

                # Find the line, cgi.fix_pathinfo=1, and change the 1 to 0.
                sed('/etc/php5/fpm/php.ini', ';cgi.fix_pathinfo=1', 'cgi.fix_pathinfo=0', use_sudo=True)
                # do nginx config
                put(StringIO(self.nginx_web_config), '/etc/nginx/sites-available/default', use_sudo=True)

                sudo('service nginx restart')
                sudo('service php5-fpm restart')
                print(green(' * Installed php5 and php5-mysql in the system.'))

            # write phpinfo for test
            put(StringIO(self.phpinfo), '{0}/info.php'.format(self.nginx_web_dir), use_sudo=True)

            print(green(' * Done'))
            print()
