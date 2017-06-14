项目列表
===============

LNMP中安装Wordpress项目
-------------------------------------------------------

介绍
~~~~~~~~~~~~~

在LNMP服务器中安装Wordpress项目

.. code-block:: bash

   -s lnmp-wordpress -p news 或者 --server lnmp-wordpress --project news

.. note:: ``-p`` 或者 ``--project`` 指代的是需要创建的wordpress项目名


数据库的创建
~~~~~~~~~~~~~~~~~~~

Wordpress默认使用Mysql作为数据库，所以我们需要提前安装好Mysql数据库

1. 登录到客户机的Mysql服务器

   .. code-block:: bash

      $ ezhost -H host -U user -P password --mysql

2. 输入数据库密码并创建数据库

   .. code-block:: bash

      mysql> create database name_you_want;

默认的配置信息
~~~~~~~~~~~~~~~~~~~

- Mysql密码: ``password``
- 项目路径: ``/var/www/html/news``