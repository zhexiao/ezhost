Usages
---------------

Use user and password to install server
----------------------

If you know your remote host's user and password, you can use the following command to install server:

.. code-block:: bash

   $ ezhost -H your_server_address -U your_server_login_user -P your_server_login_password -s server_type

.. note:: All exist **server_type** you can find from the *Servers* docs.


Use user and keyfile to install server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have your remote host's user and keyfile, you can use the following command to install server:

.. code-block:: bash

   $ ezhost -H your_server_address -U your_server_login_user -K ~/.ssh/keyfile.pem -s server_type 


Use git pull in remote server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can run the following command to update your github project in remote server:

.. code-block:: bash

   $ ezhost -H your_server_address -U your_server_login_user -P your_server_login_password --git-pull /var/www/html/project 


.. note:: ``/var/www/html/project`` is your gituhb project folder. 
