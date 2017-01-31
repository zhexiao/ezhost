Server Lists
===============

In here, we can install the most popular servers just by few commands.

|

LAMP Server
-----------------------------------------------

Introduction
~~~~~~~~~~~~~

Linux + Apache + Mysql + PHP

A "LAMP" stack is a group of open source software that is typically installed together to enable a server to host dynamic websites and web apps. This term is actually an acronym which represents the Linux operating system, with the Apache web server. The site data is stored in a MySQL database, and dynamic content is processed by PHP.


Keyword
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash
   
   -s lamp or --server lamp


Configuration
~~~~~~~~~~~~~~~~~~~

- mysql password: ``password``
- web root: ``/var/www/html``
- phpinfo path: ``/var/www/html/info.php``


Restart
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash
   
   $ sudo service apache2 restart


|

LNMP Server
-------------------------------------------

Introduction
~~~~~~~~~~~~~~~~~

Linux + Nginx + Mysql + PHP

The LNMP software stack is a group of software that can be used to serve dynamic web pages and web applications. This is an acronym that describes a Linux operating system, with an Nginx web server. The backend data is stored in MySQL and the dynamic processing is handled by PHP.


Keyword
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash
   
   -s lnmp or --server lnmp


Configuration
~~~~~~~~~~~~~~~~~~~

- nginx config path: ``/etc/nginx/sites-available/default``
- mysql password: ``password``
- web root: ``/var/www/html``
- phpinfo path: ``/var/www/html/info.php``


Restart
~~~~~~~~~~~~~~~~

.. code-block:: bash
   # for php5
   $ sudo service php5-fpm restart

   # for php7
   $ sudo service php7.0-fpm restart

   # for niginx
   $ sudo service nginx restart

.. note:: We use ``php-fpm`` as the php interpret in LNMP Server.


|

Django Basic Web Server
----------------------------------------------------------

Introduction
~~~~~~~~~~~~~~~~

Django + Mysql

Django is a powerful web framework that can help you get your Python application or website off the ground. Django includes a simplified development server for testing your code locally, but for anything even slightly production related, a more secure and powerful web server is required.


Keyword
~~~~~~~~~

.. code-block:: bash
   
   -s django -p project_name or --server django --project project_name

.. note:: if you provide the parameter ``-p project_name``. We will create ``project_name folder`` for your django web application. Otherwise the project_name will use the default name ``demo``.


Configuration
~~~~~~~~~~~~~~~

- mysql password: ``password``
- web root: ``/var/www/html``
- project root: ``/var/www/html/project_name``
- virtualenv path: ``~/.project_name``

.. note:: The ``project_name`` come from ``-p`` value. For example, if you provide ``-p zhex``. Then we will generate ``/var/www/html/zhex`` as project root.


Mysql Config
~~~~~~~~~~~~~~
Use Mysql database rather than default django database Sqlite3.

- Go to ``/var/www/html/project_name/project_name`` and edit settings.py

.. code-block:: bash
   
   $ cd /var/www/html/project_name/project_name
   $ vim settings.py

- Change DATABASES config as follows

.. code-block:: bash
   
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'HOST': 'localhost',
           'NAME' : 'your_database_name',
           'USER' : 'root',
           'PASSWORD' : 'password'
       }
   }

- Active your project virtual environment

.. code-block:: bash
   
   $ source ~/.project_name/bin/activate 

- Go to ``/var/www/html/project_name`` and running database migrate

.. code-block:: bash
   
   $ cd ..
   $ python manage.py migrate 

.. important:: Before you run `migrate`, please make sure you already create your database.


Virtualenv
~~~~~~~~~~~
Virtualenv is a tool to create isolated Python environments.

For django project, we will use virtualenv to create your project virtual environment and save your python packages inside. You can find your virtualenv folder at ``~/.project_name``.

The following command is a basic usage for your virtualenv.

.. code-block:: bash
    
   # go to your env dir
   $ cd ~/.project_name

   # active your env
   $ source bin/activate
   
   # deactive your env
   $ deactivate


|

Django Advanced Web Server
----------------------------------------------------------

Introduction
~~~~~~~~~~~~~~~~

Django + Uwsgi + Nginx + Supervisor

Django is a powerful web framework that can help you get your Python application or website off the ground. Django includes a simplified development server for testing your code locally, but for anything even slightly production related, a more secure and powerful web server is required.

In this guide, We will configure the uWSGI application container server to interface with our applications. We will then set up Nginx to reverse proxy to uWSGI, giving us access to its security and performance features to serve our apps. After that, we will install linux supervisor to control uWSGI service auto start.


Keyword
~~~~~~~~~

.. code-block:: bash
   
   -s django-uwsgi -p project_name or --server django-uwsgi --project project_name

.. note:: if you provide the parameter ``-p project_name``. We will create ``project_name folder`` for your django web application. Otherwise the project_name will use the default name ``demo``.


Configuration
~~~~~~~~~~~~~~~

Normal Config

- web root: ``/var/www/html``
- project root: ``/var/www/html/project_name``
- virtualenv path: ``~/.project_name``
- mysql password: ``password``

Server Config

- nginx config path: ``/etc/nginx/sites-enabled/default``
- uwsgi config path: ``/var/www/html/project_name/project_name.ini``
- supervisor config path: ``/etc/supervisor/conf.d/project_name_sysd.conf``

Log Config

- django normal output file: ``/var/log/project_name_out.log``
- django error output file: ``/var/log/project_name_error.log``

.. note:: The ``project_name`` come from ``-p`` value. For example, if you provide ``-p zhex``. Then we will generate ``/var/www/html/zhex`` as project root and the supervisor config path will became ``/etc/supervisor/conf.d/zhex_sysd.conf``


Virtualenv
~~~~~~~~~~~
Virtualenv is a tool to create isolated Python environments.

For django project, we will use virtualenv to create your project virtual environment and save your python packages inside. You can find your virtualenv folder at ``~/.project_name``.

The following command is a basic usage for your virtualenv.

.. code-block:: bash
    
   # go to your env dir
   $ cd ~/.project_name

   # active your env
   $ source bin/activate
   
   # deactive your env
   $ deactivate


Restart
~~~~~~~~~

.. code-block:: bash
   
   $ service nginx restart
   $ sudo supervisorctl reread && sudo supervisorctl update

.. important:: We use supervisor as the uwsgi service controller in order to auto restart. More details about supervisor: http://supervisord.org/index.html

|