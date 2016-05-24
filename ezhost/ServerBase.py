# -*- coding: utf-8 -*-
"""
Base class for all server class
"""
from fabric.api import env

from ezhost.ServerAbstract import ServerAbstract
from ezhost.ServerLists import ServerLists
from ezhost.ServerLamp import ServerLamp

class ServerBase(ServerAbstract):
    def __init__(self, args):
        # set information
        self.host_string = args.host
        self.host_user = args.user
        self.host_passwd = args.passwd
        self.server_type = args.server
        
        # initial host 
        self.init_host()

        # install 
        self.install()

    def install(self):
        """
            install the server
        """
        try:
            server = ServerLists(self.server_type)
            eval(server.name)().install()
        except Exception as e:
            raise e
       

    def init_host(self):
        """
            Initial  host 
        """
        env.host_string = self._host_string
        env.user = self._host_user
        env.password = self._host_passwd
