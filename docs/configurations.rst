Configurations
===============

This document will show you all the exist configuration of ezhost.

LAMP Server(Linux + Apache + Mysql + PHP)
---------------

Install
~~~~~~
.. code-block:: bash
   
   $ ezhost -s lamp -H 127.0.0.1:2201 -U vagrant -P vagrant

Server Configure
~~~~~~

- default mysql password: ``password``
- default web root: ``/var/www/html``
- phpinfo path: ``/var/www/html/info.php``

LNMP Server(Linux + Nginx + Mysql + PHP)
---------------

Install
~~~~~~
.. code-block:: bash
   
   $ ezhost -s lnmp -H 127.0.0.1:2201 -U vagrant -P vagrant

Server Configure
~~~~~~

- default host config path: ``/etc/nginx/sites-available/default``
- default mysql password: ``password``
- default web root: ``/var/www/html``
- phpinfo path: ``/var/www/html/info.php``

.. note:: For the php interpret, we are using php-fpm rathan then php-cgi, so when you want to restart the server, you should do ``service php5-fpm restart`` and ``service nginx restart``. 