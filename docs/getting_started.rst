Getting Started
===============

This document will show you how to get up and running with ezhost.

|

Requirement
---------------

You have to install python3 and pip3 before you install ezhost:

.. code-block:: bash

   # update system package
   $ sudo apt-get update

   # install python3 and pip3
   $ sudo apt-get install python3 python3-pip

|

Dependency Install
---------------

If you have error happens during the ezhost install, you'd better install these dependency as well.

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

After you install pip3, you can install ezhost directly from PyPI.

.. code-block:: bash

   $ sudo pip3 install ezhost
