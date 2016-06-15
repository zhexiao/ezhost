# -*- coding: utf-8 -*-
"""
This class is aim to install wordpress project in lnmp server(Linux, Nginx, Mysql and PHP) into your host.

Usage:
    $ sudo pip install ezhost
    $ ezhost -s lnmp-wordpress -p news -H 127.0.0.1:2201 -U vagrant -P vagrant

Author: Zhe Xiao

Contact: zhexiao27@gmail.com
    
Github: https://github.com/zhexiao/ezhost.git
"""
from io import StringIO

from ezhost.ServerAbstract import ServerAbstract
from ezhost.ServerLnmp import ServerLnmp

# fabric libs
from fabric.colors import red, green
from fabric.api import env, prompt, run, sudo, local, put
from fabric.contrib.files import exists, sed
from fabric.state import output
from fabric.context_managers import cd

# hide exec command
output['running'] = False


class ServerLnmpWordpress(ServerAbstract):

    def __init__(self, args):
        self.args = args
        self.project = self.args.project

    def install(self):
        # first install lnmp server
        ServerLnmp(self.args).install()

        self.install_wordpress()
        self.vagrant_workspace()

    def install_wordpress(self):
        if self.args.force or prompt(red(' * Install wordpress (y/n)?'), default='y') == 'y':
            # These two packages allow you to work with images and
            # install/update plugins and components using SSH respectively.
            sudo('sudo apt-get install php5-gd libssh2-php -y')

            # go to web root
            with cd(self.nginx_web_dir):
                # download latest wordpress   
                sudo('wget https://wordpress.org/latest.tar.gz')
                sudo('tar -zxvf latest.tar.gz')
                sudo('sudo chown -R www-data:www-data wordpress')
                # rename wordpress project
                sudo('mv wordpress {0}'.format(self.project))
                # create uploads folder
                sudo('mkdir {0}/wp-content/uploads'.format(self.project))
                sudo('chown -R www-data:www-data {0}/wp-content/uploads'.format(self.project))

            # go to nginx available config
            with cd('/etc/nginx/sites-available'):
                if not exists(self.project):
                    sudo('touch {0}'.format(self.project))
                put(StringIO(self.nginx_web_wordpress_config), self.project, use_sudo=True)

            # go to nginx enabled config
            with cd('/etc/nginx/sites-enabled'):
                if exists(self.project):
                    sudo('rm {0}'.format(self.project))

                # remove the default nginx configuration
                if exists('default'):
                    sudo('rm default')
                    
                sudo('ln -s /etc/nginx/sites-available/{0} .'.format(self.project))

            # restart server
            sudo('service nginx restart')
            sudo('service php5-fpm restart')

            print(green(' * Done'))
            print()

    def vagrant_workspace(self):
        if prompt(red(' * Are you working on the vagrant server (y/n)?'), default='y') == 'y':
            sudo('mv /var/www/html/ /vagrant/')
            sudo('cd /var/www/ && ln -s /vagrant/html/ .')
