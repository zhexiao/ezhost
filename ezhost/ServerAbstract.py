# -*- coding: utf-8 -*-
"""
Abstract class for all server class
"""

# internal libs
import os
from abc import ABCMeta, abstractmethod, abstractproperty

class ServerAbstract(metaclass=ABCMeta):
    def __init__(self):
        # host information
        self._host_string = None
        self._host_user = None
        self._host_passwd = None
        # server type
        self._server_type = None

    @property
    def host_string(self):
        """
            Host String getter
        """
        return self._host_string

    @host_string.setter
    def host_string(self, value):
        """
            Host string setter
        """
        self._host_string = value

    @property
    def host_user(self):
        """
            Host user getter
        """
        return self._host_user

    @host_user.setter
    def host_user(self, value):
        """
            Host user setter
        """
        self._host_user = value

    @property
    def host_passwd(self):
        """
            Host password getter
        """
        return self._host_passwd

    @host_passwd.setter
    def host_passwd(self, value):
        """
            Host password setter
        """
        self._host_passwd = value

    @property
    def server_type(self):
        """
            Server type getter
        """
        return self._server_type

    @server_type.setter
    def server_type(self, value):
        """
            Server type setter
        """
        self._server_type = value
 
    @property
    def command_path(self):
        """
            Currently command path
        """
        return os.path.dirname(os.path.realpath(__file__))

    @property
    def mysql_password(self):
        """
            Mysql password
        """
        return 'xiaozhe'

    @property
    def apache_web_dir(self):
        """
            default apache project dir
        """
        return '/var/www/html'

    @property
    def apache_dir_index(self):
        """
            Currently, if a user requests a directory from the server, Apache 
            will first look for a file called index.html. We want to tell our 
            web server to prefer PHP files, so we'll make Apache look for an 
            index.php file first.
        """
        long_text = """
<IfModule mod_dir.c>
    DirectoryIndex index.php index.html index.cgi index.pl index.xhtml index.htm
</IfModule>
        """
        return long_text

    @property
    def phpinfo(self):
        """
           In order to test that our system is configured properly for PHP, 
           we can create a very basic PHP script.
        """
        long_text = """
<?php
phpinfo();
?>
        """
        return long_text

    @abstractmethod
    def install(self):
        """
            All subclass need implement this function
        """
        pass
