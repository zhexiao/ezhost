Commands
===============

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