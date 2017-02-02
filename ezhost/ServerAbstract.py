# -*- coding: utf-8 -*-
import os
from abc import ABCMeta, abstractmethod, abstractproperty
import ezhost.config.apache_conf_string as apache_conf_string
import ezhost.config.php_conf_string as php_conf_string
import ezhost.config.nginx_conf_string as nginx_conf_string
import ezhost.config.django_conf_string as django_conf_string


class ServerAbstract(metaclass=ABCMeta):
    """
        Server abstract class, all server should extend from it
    """

    def __init__(self):
        # host information
        self._host_string = None
        self._host_user = None
        self._host_passwd = None
        self._host_keyfile = None
        # server type
        self._server_type = None
        self._project = None

    @property
    def host_string(self):
        """
            Returns:
                str: hostname string
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
    def host_keyfile(self):
        """
            Host keyfile getter
        """
        return self._host_keyfile

    @host_keyfile.setter
    def host_keyfile(self, value):
        """
            Host keyfile setter
        """
        self._host_keyfile = value

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
    def project(self):
        """
            project getter
        """
        return self._project

    @project.setter
    def project(self, value):
        """
            project setter
        """
        self._project = value

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
        return 'password'

    @property
    def apache_web_dir(self):
        """
            default apache project dir
        """

        return apache_conf_string.web_dir

    @property
    def nginx_web_dir(self):
        """
            default apache project dir
        """

        return nginx_conf_string.web_dir

    @property
    def apache_dir_index(self):
        """
            Currently, if a user requests a directory from the server, Apache
            will first look for a file called index.html. We want to tell our
            web server to prefer PHP files, so we'll make Apache look for an
            index.php file first.
        """

        return apache_conf_string.module_index_str

    @property
    def phpinfo(self):
        """
           In order to test that our system is configured properly for PHP,
           we can create a very basic PHP script.
        """

        return php_conf_string.phpinfo_str

    @property
    def nginx_web_config(self):
        """
           Nginx web config
        """

        return nginx_conf_string.simple_web_config.format(self.nginx_web_dir)

    @property
    def nginx_php7_web_config(self):
        """
           Nginx web config
        """

        return nginx_conf_string.simple_php7_web_config.format(self.nginx_web_dir)

    @property
    def nginx_web_ssl_config(self):
        """
           Nginx web ssl config
        """

        dt = [self.nginx_web_dir, self.nginx_ssl_dir]
        return nginx_conf_string.simple_ssl_web_conf.format(dt=dt)

    @property
    def python_env_dir(self):
        """
            Python virtualenv dir
        """
        return '~/.{0}'.format(self.project)

    @property
    def django_uwsgi_ini(self):
        """
           This ini file is django uwsgi configuration
        """

        return django_conf_string.uwsgi_ini_conf

    @property
    def django_uwsgi_with_nginx(self):
        """
           This ini file nginx configuration with uwsgi application
        """

        return django_conf_string.uwsgi_nginx_conf.format(self.project)

    @property
    def supervisor_uwsgi_ini(self):
        """
           supervisor control uwsgi configuration
        """

        return django_conf_string.uwsgi_supervisor_conf

    @property
    def supervisor_etc_dir(self):
        """
            supervisor control config dir
        """
        return django_conf_string.supervisor_dir

    @property
    def supervisor_config_dir(self):
        """
            supervisor control config dir
        """
        return django_conf_string.supervisor_conf_dir

    @property
    def nginx_ssl_dir(self):
        """
            ssl directory
        """
        return nginx_conf_string.web_ssl_dir

    @property
    def nginx_web_wordpress_config(self):
        """
           Nginx web wordpress config
        """

        return nginx_conf_string.wordpress_web_conf.format(
            self.nginx_web_dir, self.project
        )

    @property
    def nginx_php7_web_wordpress_config(self):
        """
           Nginx web wordpress config
        """

        return nginx_conf_string.wordpress_php7_web_conf.format(
            self.nginx_web_dir, self.project
        )

    @abstractmethod
    def install(self):
        """
            All subclass need implement this function
        """
        pass
