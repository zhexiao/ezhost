命令行列表
===============

默认安装
--------------------

默认安装就是不在询问用户，直接执行安装程序

.. code-block:: bash

   -f 或者 --force


git代码更新
--------------------

通过主机控制远程客户机的代码进行更新

.. code-block:: bash

   -gp /var/www/html/project 或者 --git-pull /var/www/html/project

.. note:: 其中 ``/var/www/html/project`` 是你的客户机git代码的保存目录


登录到远程客户机
----------------------

通过主机登录到客户机

.. code-block:: bash

   -login 或者 --login

登录到远程客户机的Mysql服务器
-------------------------------

直接通过主机登录到客户机的Mysql服务器，然后就可以操作Mysql服务器的一些指令

.. code-block:: bash

   -my 或者 --mysql

查看客户机运行中的端口
-------------------------------

打印客户机中正在运行的端口

.. code-block:: bash

   -ap 或者 --active-port