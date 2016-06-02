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
        self._host_keyfile = None
        # server type
        self._server_type = None
        self._project = None

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
        return '/var/www/html'

    @property
    def nginx_web_dir(self):
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
        long_text = """<IfModule mod_dir.c>
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
        long_text = """<?php
phpinfo();
?>
        """
        return long_text

    @property
    def nginx_web_config(self):
        """
           Nginx web config
        """
        long_text = """server 
{
    listen 80 default_server;
    listen [::]:80 default_server;

    root %s;
    autoindex on;
    # Add index.php to the list if you are using PHP
    index index.php index.html index.htm index.nginx-debian.html;

    server_name localhost;

    #location / {
    #    try_files $uri $uri/ =404;
    #}

    # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
    location ~ \.php$ {
       include snippets/fastcgi-php.conf;   
       # With php5-cgi alone:
       # fastcgi_pass 127.0.0.1:9000;
       # With php5-fpm:
       fastcgi_pass unix:/var/run/php5-fpm.sock;
    }

    # deny access to .htaccess files, if Apache's document root
    # concurs with nginx's one
    #location ~ /\.ht {
    #    deny all;
    #}
}
        """

        long_text = long_text % (self.nginx_web_dir)
        return long_text

    @property
    def python_env_dir(self):
        """
            Python virtualenv dir
        """
        return '{0}/{1}/env'.format(self.nginx_web_dir, self.project)

    @property
    def django_uwsgi_ini(self):
        """
           This ini file is django uwsgi configuration
        """
        long_text = """[uwsgi]
chdir = {0}/{1}
home = {2}
module = {1}.wsgi:application

uid = vagrant
gid = www-data

master = true
processes = 5

socket = /tmp/{1}.sock
chmod-socket = 664
vacuum = true
        """
        return long_text

    @property
    def django_uwsgi_with_nginx(self):
        """
           This ini file nginx configuration with uwsgi application
        """
        long_text = """server {
    listen 80;
    server_name localhost;

    location = /favicon.ico { 
        access_log off; 
        log_not_found off; 
    }

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/tmp/%s.sock;
    }
}
        """
        long_text = long_text  % (self.project)
        return long_text

    @property
    def supervisor_uwsgi_ini(self):
        """
           supervisor control uwsgi configuration 
        """
        long_text = """[program:{0}]
; Set full path to program if using virtualenv
command=uwsgi --ini {1}/{0}.ini

; The directory to your Django project
directory={1}

; Supervisor will start as many instances of this program as named by numprocs
numprocs=1

; Put process stdout output in this file
stdout_logfile=/var/log/{0}_out.log

; Put process stderr output in this file
stderr_logfile=/var/log/{0}_error.log

; If true, this program will start automatically when supervisord is started
autostart=true

; May be one of false, unexpected, or true. If false, the process will never
; be autorestarted. If unexpected, the process will be restart when the program
; exits with an exit code that is not one of the exit codes associated with this
; process’ configuration (see exitcodes). If true, the process will be
; unconditionally restarted when it exits, without regard to its exit code.
autorestart=true

; The total number of seconds which the program needs to stay running after
; a startup to consider the start successful.
startsecs=2

; Need to wait for currently executing tasks to finish at shutdown.
; Increase this if you have very long running tasks.
stopwaitsecs=2

; When resorting to send SIGKILL to the program to terminate it
; send SIGKILL to its whole process group instead,
; taking care of its children as well.
killasgroup=true

; if your broker is supervised, set its priority higher, so it starts first
priority=998   
        """
        return long_text

    @property
    def supervisor_config_dir(self):
        """
            supervisor control config dir
        """
        return '/etc/supervisor/conf.d'

    @abstractmethod
    def install(self):
        """
            All subclass need implement this function
        """
        pass
