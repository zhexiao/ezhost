Server Lists
===============

In here, i will show you all exist server command.

LAMP Server(Linux + Apache + Mysql + PHP)
---------------

Install
~~~~~~
.. code-block:: bash
   
   $ ezhost -s lamp -H your_server_address -U your_server_login_user -P your_server_login_password

Server Configure
~~~~~~

- default mysql password: ``password``
- default web root: ``/var/www/html``
- phpinfo path: ``/var/www/html/info.php``

Server Restart
~~~~~~

.. code-block:: bash
   
   $ sudo service apache2 restart



LNMP Server(Linux + Nginx + Mysql + PHP)
---------------

Install
~~~~~~
.. code-block:: bash
   
   $ ezhost -s lnmp -H your_server_address -U your_server_login_user -P your_server_login_password

Server Configure
~~~~~~

- default host config path: ``/etc/nginx/sites-available/default``
- default mysql password: ``password``
- default web root: ``/var/www/html``
- phpinfo path: ``/var/www/html/info.php``

Server Restart
~~~~~~
.. code-block:: bash
   
   $ sudo service php5-fpm restart
   $ sudo service nginx restart

.. note:: For the php interpret in LNMP Server, we are using ``php-fpm`` rathan then ``php-cgi``.



Django Web Server(Django + Uwsgi + Nginx + Supervisor)
---------------

Install
~~~~~~
.. code-block:: bash
   
   $ ezhost -s django-uwsgi -p project_name -H your_server_address -U your_server_login_user -P your_server_login_password

Server Configure
~~~~~~
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
~~~~~~
For django project, we will auto use virtualenv to create a virtual environment for store all these installed packages. You can find your virtualenv path from ``Server Configure``.

The following command is a basic usage for your virtualenv.

.. code-block:: bash
    
   # go to your project dir
   $ cd /var/www/html/project_name

   # active your env
   $ source env/bin/activate
   
   # if you want to deactive your env
   $ deactivate

Server Restart
~~~~~~
.. code-block:: bash
   
   $ service nginx restart
   $ sudo supervisorctl reread && sudo supervisorctl update

.. note:: we are use supervisor to control the uwsgi service auto restart. More details about supervisor: http://supervisord.org/index.html
