Usages
===============

Before you use ezhost, you have to connect to your host at first, in here i will show you three ways to connect your host

Use user and password
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you know your remote host's user and password, you can use the following command to install server:

.. code-block:: bash

   $ ezhost -H your_server_address -U your_server_login_user -P your_server_login_password


Use user and keyfile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have your remote host's user and keyfile, you can use the following command to install server:

.. code-block:: bash

   $ ezhost -H your_server_address -U your_server_login_user -K ~/.ssh/keyfile.pem


Use config file 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Assuming you have a config file **development.ini** in **/var/www/html** folder.

.. code-block:: bash
   :linenos:

   [ezhost]
   host=your_server_address
   user=your_server_login_user
   passwd=your_server_login_password

.. note:: If you want to change **passwd** to **keyfile**, just need to replace ``passwd=your_server_login_password`` to ``keyfile=~/.ssh/keyfile.pem``.

After you have ezhost config file, you can use the following command to run it:

.. code-block:: bash

   $ ezhost -c /var/www/html/development.ini

