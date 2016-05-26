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
