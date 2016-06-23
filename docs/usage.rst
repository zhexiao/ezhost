Usages
===============

This document will show you all exist options in ezhost.

Use user and password
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you know your remote host's user and password, you can use the following command to install server:

.. code-block:: bash

   $ ezhost -H your_server_address -U your_server_login_user -P your_server_login_password -s server_type

.. note:: All exist **server_type** you can find from the *Servers* docs.


Use user and keyfile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have your remote host's user and keyfile, you can use the following command to install server:

.. code-block:: bash

   $ ezhost -H your_server_address -U your_server_login_user -K ~/.ssh/keyfile.pem -s server_type 


Use config file 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Assuming you have a config file **development.ini** in **/var/www/html** folder. Then you should have the following format in **development.ini**:

.. highlight:: python
   :linenothreshold: 5

    [ezhost]
    host=127.0.0.1:2200
    user=vagrant
    passwd=vagrant




.. code-block:: bash

   $ ezhost -H your_server_address -U your_server_login_user -K ~/.ssh/keyfile.pem **-c /var/www/html/development.ini**



Use git pull
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can run the following command to update your github project in remote server:

.. code-block:: bash

   $ ezhost -H your_server_address -U your_server_login_user -P your_server_login_password --git-pull /var/www/html/project 


.. note:: ``/var/www/html/project`` is your gituhb project folder. 


Use mysql
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can run the following command to login to your remote mysql server:

.. code-block:: bash

   $ ezhost -H your_server_address -U your_server_login_user -P your_server_login_password -my