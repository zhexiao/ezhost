Server Lists
===============

In here, i will show you all exist server command.

LAMP Server
-----------------------------------------------

Introduction
~~~~~~~~~~~~~

Linux + Apache + Mysql + PHP

A "LAMP" stack is a group of open source software that is typically installed together to enable a server to host dynamic websites and web apps. This term is actually an acronym which represents the Linux operating system, with the Apache web server. The site data is stored in a MySQL database, and dynamic content is processed by PHP.


Keyword
~~~~~~~~~~~~~~~~~~~

**-s lamp**

Configuration
~~~~~~~~~~~~~~~~~~~

- mysql password: ``password``
- web root: ``/var/www/html``
- phpinfo path: ``/var/www/html/info.php``


Restart
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash
   
   $ sudo service apache2 restart



LNMP Server
-------------------------------------------

Introduction
~~~~~~~~~~~~~~~~~

Linux + Nginx + Mysql + PHP

The LNMP software stack is a group of software that can be used to serve dynamic web pages and web applications. This is an acronym that describes a Linux operating system, with an Nginx web server. The backend data is stored in MySQL and the dynamic processing is handled by PHP.


Install
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash
   
   $ ezhost -s lnmp -H your_server_address -U your_server_login_user -P your_server_login_password


Configuration
~~~~~~~~~~~~~~~~~~~

- web config path: ``/etc/nginx/sites-available/default``
- mysql password: ``password``
- web root: ``/var/www/html``
- phpinfo path: ``/var/www/html/info.php``


Restart
~~~~~~~~~~~~~~~~

.. code-block:: bash
   
   $ sudo service php5-fpm restart
   $ sudo service nginx restart

.. note:: For the php interpret in LNMP Server, we are use ``php-fpm`` rathan then ``php-cgi``.



Django Web Server
----------------------------------------------------------

Introduction
~~~~~~~~~~~~~~~~

Django + Uwsgi + Nginx + Supervisor

Django is a powerful web framework that can help you get your Python application or website off the ground. Django includes a simplified development server for testing your code locally, but for anything even slightly production related, a more secure and powerful web server is required.

In this guide, We will configure the uWSGI application container server to interface with our applications. We will then set up Nginx to reverse proxy to uWSGI, giving us access to its security and performance features to serve our apps. After that, we will install linux supervisor to control uWSGI service auto start.


Install
~~~~~~~~~

.. code-block:: bash
   
   $ ezhost -s django-uwsgi -p project_name -H your_server_address -U your_server_login_user -P your_server_login_password

.. note:: if you give us the parameter ``-p project_name``. Then we will create a ``project_name folder`` for your django web application. Otherwise the project_name will use the default value ``demo``.


Configuration
~~~~~~~~~~~~~~~

- nginx config path: ``/etc/nginx/sites-enabled/default``
- web root: ``/var/www/html``
- project root: ``/var/www/html/project_name``
- virtualenv path: ``/var/www/html/project_name/env``
- uwsgi config path: ``/var/www/html/project_name/project_name.ini``
- supervisor config path: ``/etc/supervisor/conf.d/project_name_sysd.conf``
- django normal output file: ``/var/log/project_name_out.log``
- django error output file: ``/var/log/project_name_error.log``

.. note:: All the ``project_name`` in the above docs will convert to your ``-p`` value. For example, if you indicate ``-p zhex``. Then the project root will be ``/var/www/html/zhex``, the supervisor config path will be ``/etc/supervisor/conf.d/zhex_sysd.conf`` and so on...


Virtualenv
~~~~~~~~~~~

For django project, we will auto use virtualenv to create a virtual environment to save all these installed packages. You can find your virtualenv folder at ``/var/www/html/project_name/env``.

The following command is a basic usage for your virtualenv.

.. code-block:: bash
    
   # go to your project dir
   $ cd /var/www/html/project_name

   # active your env
   $ source env/bin/activate
   
   # if you want to deactive your env
   $ deactivate

Restart
~~~~~~~~~

.. code-block:: bash
   
   $ service nginx restart
   $ sudo supervisorctl reread && sudo supervisorctl update

.. note:: we are use supervisor to control the uwsgi service auto restart. More details about supervisor: http://supervisord.org/index.html
