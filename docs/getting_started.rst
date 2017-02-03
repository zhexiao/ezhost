Getting Started
===============

This document will show you how to get up and running with ezhost.

|

Python and Pip Install
-------------------------

You have to install python3 and pip3 before you install ezhost:

.. code-block:: bash

   # update system package
   $ sudo apt-get update

   # install python3 and pip3
   $ sudo apt-get install python3 python3-pip

|

Dependency Install
---------------------

If you have any errors during the ezhost installing, you'd better install these dependencies as well.

.. code-block:: bash

   # update python tool
   $ pip3 install --upgrade setuptools
   $ pip3 install --upgrade distribute

   # install cryptography
   $ sudo apt-get install build-essential libssl-dev libffi-dev python-dev
   $ pip3 install cryptography
  
|

Ezhost Install
---------------

if your working environment is python>=3.*, run the following command for install.

.. code-block:: bash
  
   $ sudo pip3 install ezhost

If your working environment is python2, run the following command for setup virtualenv.

.. code-block:: bash
  
   $ sudo pip install virtualenv
   $ virtualenv -p python3 ~/.ezhost
   $ source ~/.ezhost/bin/activate
   $ pip install ezhost

