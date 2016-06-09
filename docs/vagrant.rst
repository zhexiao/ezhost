Ezhost with Vagrant
======================



Virtualenv
---------------

We recommend use virtual environment for your packages. We can use virtualenv to generate virtual environment:

Using virtualenv to create your environment
~~~~~~

.. code-block:: bash
   
   # generate your env(for python3)
   $ virtualenv -p python3 env --always-copy

   # if you want to use python2
   $ virtualenv env 
   
After you generate your virtualenv, you can use the following commands to active your env:

.. code-block:: bash
   
   # active your env
   $ source env/bin/activate
   
   # deactive your env
   $ deactivate
   

