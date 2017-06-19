开始安装
========

安装python3-pip
-------------------------

Ezhost是基于Python3开发的，在安装Ezhost之前，需要安装python3-pip。

.. code-block:: bash

   # 安装python3-pip
   $ sudo apt-get install python3-pip

安装Ezhost
-------------------------

在安装Ezhost之前，需要安装一些Ubuntu中的依赖库

.. code-block:: bash

   # 安装依赖库
   $ sudo apt-get install libffi-dev libssl-dev
   $ sudo pip3 install cryptography pynacl

通过pip3安装Ezhost

.. code-block:: bash

   # 安装Ezhost
   $ sudo pip3 install ezhost