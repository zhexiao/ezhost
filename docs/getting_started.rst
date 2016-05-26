Getting Started
===============

This document will show you how to get up and running with ezhost.


Requirement
---------------

You have to install python3 and pip3 before you install ezhost:

.. code-block:: bash
   
   # update system package
   $ sudo apt-get update 
   
   # install python3, pip3 and python3 venv
   $ sudo apt-get install python3
   $ sudo apt-get install python3-pip
   $ sudo apt-get install python3.4-venv


Virtualenv
---------------

We recommend using virtual environment for your packages. For python3.4, we can using pyvenv to generate virtualenv:

.. code-block:: bash
   
   # generate your virtualenv
   $ python3 -m venv env 
   Or 
   $ pyvenv-3.4 env
   
After you generate your virtualenv, you can using the following command to active your env:

.. code-block:: bash
   
   # active your env
   $ source env/bin/activate
   
   # deactive your env
   $ deactivate
   

Install
---------------

You can install ezhost directly from PyPI using:

.. code-block:: bash
   
   $ pip install ezhost


Basic Usage
---------------

After you installed ezhost from pip, you can easy to running the following command to generate a new server:

.. code-block:: bash
   
   $ ezhost -s lamp -H 127.0.0.1:2201 -U vagrant -P vagrant
   
The above code will generate a ``LAMP`` server(Linux, Apache, Mysql and PHP5) in ``Vagrant``. ``-H`` indicate your host address. ``-U`` indicate your host login user. ``-P`` indicate your host passowrd for login.


.. code-block:: bash
   
   $ ezhost -s lamp -H ec2-11-111-11-111.compute-1.amazonaws.com -U ubuntu -K ~/.ssh/keyfile.pem
   
The above code will generate a ``LAMP`` server(Linux, Apache, Mysql and PHP5) in ``AWS EC2``. ``-H`` indicate your host address. ``-U`` indicate your host login user. ``-K`` indicate your host keyfile.

.. note:: The installed lamp server is a very basic server. Run ``sudo apt-cache search php5-`` find what kind of php module you need. Then run ``sudo apt-get install package1 package2 ...`` to install it.
