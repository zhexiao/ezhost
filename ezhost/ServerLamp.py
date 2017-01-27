# -*- coding: utf-8 -*-
"""
This class is aim to install lamp server(Linux, Apache, Mysql and PHP) into your
local environment.

Usage:
    $ sudo pip install ezhost
    $ ezhost -s lamp -H 127.0.0.1:2201 -U vagrant -P vagrant

Author: Zhe Xiao
Github: https://github.com/zhexiao/ezhost.git
"""

from io import StringIO

from ezhost.ServerCommon import ServerCommon

# fabric libs
from fabric.colors import red, green
from fabric.api import prompt, sudo, put
from fabric.state import output

# hide exec command
output['running'] = False


class ServerLamp(ServerCommon):

    def __init__(self, args):
        self.args = args

    def install(self):
        self.update_sys()
        self.install_apache()
        self.install_mysql()
        self.install_php()

    def update_sys(self):
        if self.args.force or prompt(red(' * Update system package (y/n)?'), default='y') == 'y':
            self.common_update_sys()

    def install_apache(self):
        if self.args.force or prompt(red(' * Install Apache2 (y/n)?'), default='y') == 'y':
            self.common_install_apache2()

    def install_mysql(self):
        if self.args.force or prompt(red(' * Install MySql (y/n)?'), default='y') == 'y':
            self.common_install_mysql()

    def install_php(self):
        if self.args.force or prompt(red(' * Install PHP (y/n)?'), default='y') == 'y':
            try:
                sudo('apt-get install php5 php5-cli php5-mysql php5-gd php5-curl libapache2-mod-php5 php5-mcrypt -y')

                # do apache config
                put(StringIO(self.apache_dir_index), '/etc/apache2/mods-enabled/dir.conf', use_sudo=True)

                sudo('service apache2 restart')
                print(green(' * Installed php5 and php5-mysql in the system.'))
            except:
                print(red(' * Install php5 and php5-mysql failed.'))

            # write phpinfo for test
            put(StringIO(self.phpinfo), '{0}/info.php'.format(self.apache_web_dir), use_sudo=True)

            print(green(' * Done'))
            print()
