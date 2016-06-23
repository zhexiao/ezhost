Project Lists
===============

In here, i will show you all exist projects in ezhost.

Wordpress with LNMP 
-------------------------------------------------------

Introduction
~~~~~~~~~~~~~
``WordPress`` is web software you can use to create a beautiful website, blog, or app. We like to say that WordPress is both free and priceless at the same time.

The core software is built by hundreds of community volunteers, and when you’re ready for more there are thousands of plugins and themes available to transform your site into almost anything you can imagine. Over 60 million people have chosen WordPress to power the place on the web they call “home” — we’d love you to join the family.


Keyword
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   $ -s lnmp-wordpress -p news

.. note:: ``-p news`` meaning ezhost will save all wordpress files into ``news`` folder. If you are not use ``-p`` flag, ezhost will use the default folder name ``demo``. 


Create Database 
~~~~~~~~~~~~~~~~~~~

As we know, wordpress use Mysql to save data. That's meaning when you project install finished, you have to create a database for mysql to save wordpress data. 

1. Login your remote mysql server 

   .. code-block:: bash

      $ ezhost -H your_server_address -U your_server_login_user -P your_server_login_password -my 

2. Use **password** as your mysql password to login 

3. Create a database

   .. code-block:: bash

      mysql> create database name_you_want;

4. Check your database

   .. code-block:: bash

      mysql> show databases;


Install Wordpress Site 
~~~~~~~~~~~~~~~~~~~~~~~

After you follow the above docs, you just need to open your server ip address on browser. Wordpress guide will help you to install it.


Configuration
~~~~~~~~~~~~~~~~~~~

- mysql password: ``password``
- web root: ``/var/www/html``
