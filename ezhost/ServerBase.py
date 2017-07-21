# -*- coding: utf-8 -*-
"""
Base class for all server class
"""
from fabric.api import env

from ezhost.ServerAbstract import ServerAbstract
from ezhost.ServerLists import ServerLists
from ezhost.ServerCommand import ServerCommand


class DynamicImporter:
    """
    Dynamic import module and call class
    """
    def __init__(self, module_name, class_name, **kwargs):
        args = kwargs.get('args')
        configure = kwargs.get('configure')

        module_name = __import__(module_name)
        my_class = getattr(module_name, class_name)
        my_class(args, configure=configure).install()


class ServerBase(ServerAbstract):
    """
    Server command bootstrap class
    """

    def __init__(self, args, configure_obj, **kwargs):
        self.args = args
        self.configure_obj = configure_obj
        self.configure = kwargs.get('configure')

        # set common parameters
        self.server_type = self.args.server
        # parser parameters
        self._parse_parameters()

        # initial host
        self.init_host()

        # install
        self.install()

    def _parse_parameters(self):
        # set args from commmand parser
        if self.configure_obj is None:
            self.host_string = self.args.host
            self.host_user = self.args.user
            self.host_passwd = self.args.passwd
            self.host_keyfile = self.args.keyfile

        # set args from config file parser
        else:
            try:
                self.host_string = self.configure_obj['host']
                self.host_user = self.configure_obj['user']
            except:
                raise KeyError('缺少必要的登录信息')

            try:
                self.host_keyfile = self.configure_obj['keyfile']
            except:
                self.host_keyfile = None

            try:
                self.host_passwd = self.configure_obj['passwd']
            except:
                self.host_passwd = None

            if self.host_passwd is None and self.host_keyfile is None:
                raise KeyError('缺少必要的登录信息')

    def init_host(self):
        """
            Initial host
        """
        env.host_string = self.host_string
        env.user = self.host_user
        env.password = self.host_passwd
        env.key_filename = self.host_keyfile

    def install(self):
        """
        install the server
        """
        try:
            if self.args.server is not None:
                server = ServerLists(self.server_type)
                DynamicImporter(
                    'ezhost',
                    server.name,
                    args=self.args,
                    configure=self.configure
                )
            else:
                ServerCommand(self.args)
        except Exception as e:
            raise e
