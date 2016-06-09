Getting Started
===============

This document will show you how to get up and run with ezhost.


Requirement
---------------

You have to install python3 and pip3 before you install ezhost:

.. code-block:: bash
   
   # update system package
   $ sudo apt-get update 
   
   # install python3 and pip3 
   $ sudo apt-get install python3 python3-pip


Install
---------------

After you install pip3, you can install ezhost directly from PyPI. 

.. code-block:: bash
  
   $ sudo pip3 install ezhost


Basic Examples
---------------

Using login user and password to create server
~~~~~~

If you have the login user and password for your remote host server, you can easy to install a ``lamp(Linux + Apache + Mysql + PHP)`` server inside it.

.. code-block:: bash
   
   $ ezhost -s lamp -H your_server_address -U your_server_login_user -P your_server_login_password
   

Using login user and keyfile to create server
~~~~~~

If you have the keyfile to login your remote host server, you can easy to install a ``lamp`` server by using the following command.

.. code-block:: bash
   
   $ ezhost -s lamp -H your_server_address -U your_server_login_user -K ~/.ssh/keyfile.pem
   
.. note:: The ``~/.ssh/keyfile.pem`` keyfile is just a example, each server may have a different name for his keyfile.

Doing git pull on the remote server
~~~~~~

If you do not want to login to your remote server to do git pull on your project. You can easy to run the following command to do ``git pull``.

.. code-block:: bash
   
   $ ezhost --git-pull /var/www/html/project -H your_server_address -U your_server_login_user -P your_server_login_password
   
The above code will go to ``/var/www/html/project`` folder and running ``git pull`` to make your github project code up to date.

.. note:: If you are use server keyfile rather than password to login your remote server, you just need to change ``-P`` to ``-K``.
