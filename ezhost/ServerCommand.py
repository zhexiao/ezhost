# -*- coding: utf-8 -*-
"""
This class is aim to exec all command on the server

Usage:
    $ sudo pip install ezhost
    $ ezhost -gp /var/www/html -H 127.0.0.1:2201 -U vagrant -P vagrant

Author: Zhe Xiao

Contact: zhexiao27@gmail.com
    
Github: https://github.com/zhexiao/ezhost.git
"""

from ezhost.ServerAbstract import ServerAbstract

# fabric libs
from fabric.colors import red, green
from fabric.api import env, prompt, run, sudo, local, put
from fabric.contrib.files import exists
from fabric.state import output

# hide exec command
output['running'] = False

class ServerCommand(ServerAbstract):
    def __init__(self, args):
        self.args = args

        # parse args
        self.dispatch_args()

    def dispatch_args(self):
        if self.args.git_pull is not None:
            self.git_pull()

        if self.args.login_mysql:
            self.login_mysql()

        if self.args.login_server:
            self.login_server()

    def install(self):
        pass

    def git_pull(self):
        """
        Doing git pull code from github
        """
        run('cd {0} && git pull'.format(self.args.git_pull))

    def login_mysql(self):
        """
        Login to remote mysql server
        """
        run('mysql -u root -p')

    def login_server(self):
        """
        Login to server
        """
        local('ssh -i {0} {1}@{2}'.format(env.key_filename, env.user, env.host_string))