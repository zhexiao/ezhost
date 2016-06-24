Usages
===============

Before you use ezhost, you have to connect to your host at first, in here i will show you three ways to connect your host.

#. Use user and password
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you know your remote host's user and password, you can use the following command to install server:

.. code-block:: bash

   $ ezhost -H host -U user -P password [keyword]


#. Use user and keyfile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have your remote host's user and keyfile, you can use the following command to install server:

.. code-block:: bash

   $ ezhost -H host -U user -K ~/.ssh/keyfile.pem [keyword]


#. Use config file 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Assuming you have a config file **development.ini** in **/var/www/html** folder.

.. code-block:: bash
   :linenos:

   [ezhost]
   host=host
   user=user
   passwd=password

.. note:: If you want to change **passwd** to **keyfile**, just need to replace ``passwd=password`` to ``keyfile=~/.ssh/keyfile.pem``.

After you have ezhost config file, you can use the following command to run it:

.. code-block:: bash

   $ ezhost -c /var/www/html/development.ini [keyword]


#. Code analysis
~~~~~~~~~~~~~~~~~~~~~~~

.. glossary::

   -H host_address
      require your host address

   -U host_user
      require your host login user

   -P host_password
      require your host login password

   -K host_keyfile
      require your host keyfile path

   -c config_path
      require your config file path

.. warning:: **[keyword]** will be replaced by command keyword, server keyword or project keyword. For example, ``-s lamp``, ``-s django-uwsgi -p project_name`` and so on ...


#. Basic Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are two examples about replace the **[keyword]** as a exist keyword.

Install LAMP Server
--------------------

.. code-block:: bash

   $ ezhost -c /var/www/html/development.ini -s lamp

.. note:: In here, we replace **[keyword]**  as ``-s lamp``.


Install Django Server
----------------------

.. code-block:: bash

   $ ezhost -c /var/www/html/development.ini -s django-uwsgi -p project_name

.. note:: In here, we replace **[keyword]**  as ``-s django-uwsgi -p project_name``.