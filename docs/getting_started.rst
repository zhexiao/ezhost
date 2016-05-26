Getting Started
===============

This document will show you how to get up and running with ezhost.

Requirement
---------------

You have to install python3 and pip3 before you install ezhost:

.. code-block:: bash
   
   $ sudo apt-get update 
   $ sudo apt-get install python3
   $ sudo apt-get install python3-pip
   $ sudo apt-get install python3.4-venv

Install
---------------

We recommend using virtual environment for your installed packages. For python3.4, we can using pyvenv to generate virtualenv:

.. code-block:: bash
   
   $ python3 -m venv env 
   Or 
   $ pyvenv-3.4 env

You can install ezhost directly from PyPI using:

.. code-block:: bash
   
   $ python3 -m venv env
   $ pip install ezhost
