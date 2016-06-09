Server Lists
===============

In here, i will show you all exist server command.

LAMP Server(Linux + Apache + Mysql + PHP)
-----------------------------------------------

Introduction
~~~~~~~~~~~~~
A "LAMP" stack is a group of open source software that is typically installed together to enable a server to host dynamic websites and web apps. This term is actually an acronym which represents the Linux operating system, with the Apache web server. The site data is stored in a MySQL database, and dynamic content is processed by PHP.


Install
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash
   
   $ ezhost -s lamp -H your_server_address -U your_server_login_user -P your_server_login_password


Configuration
~~~~~~~~~~~~~~~~~~~

- mysql password: ``password``
- web root: ``/var/www/html``
- phpinfo path: ``/var/www/html/info.php``


Restart
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash
   
   $ sudo service apache2 restart



LNMP Server(Linux + Nginx + Mysql + PHP)
-------------------------------------------

Introduction
~~~~~~~~~~~~~~~~~

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



Django Web Server(Django + Uwsgi + Nginx + Supervisor)
----------------------------------------------------------

Install
~~~~~~~~~

.. code-block:: bash
   
   $ ezhost -s django-uwsgi -p project_name -H your_server_address -U your_server_login_user -P your_server_login_password

Configuration
~~~~~~~~~~~~~~~

From above install command, if you indicate ``-p project_name``. We will create a ``project_name`` folder for your django web application, otherwise the project_name will use the default name ``demo``.

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

For django project, we will auto use virtualenv to create a virtual environment for store all these installed packages. You can find your virtualenv path from ``Server Configure``.

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
