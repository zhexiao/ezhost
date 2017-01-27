# -*- coding: utf-8 -*-
"""
This class is aim to install wordpress project in lnmp server(Linux, Nginx, Mysql and PHP) into your host.

Usage:
    $ sudo pip install ezhost
    $ ezhost -s lnmp-wordpress -p news -H 127.0.0.1:2201 -U vagrant -P vagrant

Author: Zhe Xiao
Github: https://github.com/zhexiao/ezhost.git
"""
from io import StringIO

# fabric libs
from fabric.colors import red, green
from fabric.api import prompt, sudo, put
from fabric.contrib.files import exists
from fabric.state import output
from fabric.context_managers import cd

from ezhost.ServerCommon import ServerCommon
from ezhost.ServerLnmp import ServerLnmp

# hide exec command
output['running'] = False


class ServerLnmpWordpress(ServerCommon):

    def __init__(self, args):
        self.args = args
        self.project = self.args.project

    def install(self):
        # install lnmp server
        ServerLnmp(self.args).install()
        self.install_wordpress()

    def install_wordpress(self):
        if self.args.force or prompt(red(' * Install Wordpress (y/n)?'), default='y') == 'y':
            # create project web server config file if not exist
            with cd('/etc/nginx/sites-available'):
                if not exists(self.project):
                    sudo('touch {0}'.format(self.project))

                # check the php version is php5 or php7
                try:
                    sudo('php5-fpm -v')
                    # save wordpress config
                    put(StringIO(self.nginx_web_wordpress_config), self.project, use_sudo=True)
                except:
                    sudo('php-fpm7.0 -v')
                    # save wordpress config
                    put(StringIO(self.nginx_php7_web_wordpress_config), self.project, use_sudo=True)

            # go to web root
            with cd(self.nginx_web_dir):
                # download latest wordpress, extract and change mode
                sudo('wget https://wordpress.org/latest.tar.gz')
                sudo('tar -zxvf latest.tar.gz')
                sudo('sudo chown -R www-data:www-data wordpress')

                # rename wordpress project
                sudo('mv wordpress {0}'.format(self.project))

                # create uploads folder
                sudo('mkdir {0}/wp-content/uploads'.format(self.project))
                sudo('chown -R www-data:www-data {0}/wp-content/uploads'.format(self.project))

            # go to nginx enabled config
            with cd('/etc/nginx/sites-enabled'):
                if exists(self.project):
                    sudo('rm {0}'.format(self.project))

                # remove the default nginx config
                if exists('default'):
                    sudo('rm default')

                # move project web server config file from avaiable to enable folder
                sudo('ln -s /etc/nginx/sites-available/{0} .'.format(self.project))

            # restart server
            try:
                sudo('service php5-fpm restart')
            except:
                sudo('service php7.0-fpm restart')
            sudo('service nginx restart')

            print(green(' * Installed Wordpress project {0} in the system.'.format(self.project)))

            print(green(' * Done'))
            print()

    def vagrant_workspace(self):
        if prompt(red(' * Are you working on the vagrant server (y/n)?'), default='y') == 'y':
            sudo('mv /var/www/html/ /vagrant/')
            sudo('cd /var/www/ && ln -s /vagrant/html/ .')
