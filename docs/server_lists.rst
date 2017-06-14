服务器列表
===============

LAMP服务器
-----------------------------------------------

介绍
~~~~~~~~~~~~~

Linux + Apache + Mysql + PHP

.. code-block:: bash
   
   -s lamp 或者 --server lamp

默认的配置信息
~~~~~~~~~~~~~~~~~~~

- Mysql密码: ``password``
- Web工作目录: ``/var/www/html``
- phpinfo路径: ``/var/www/html/info.php``

服务器重启
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash
   
   $ sudo service apache2 restart

LNMP Server
-------------------------------------------

介绍
~~~~~~~~~~~~~~~~~

Linux + Nginx + Mysql + PHP

.. code-block:: bash
   
   -s lnmp 或者 --server lnmp

默认的配置信息
~~~~~~~~~~~~~~~~~~~

- nginx配置文件路径: ``/etc/nginx/sites-available/default``
- Mysql密码: ``password``
- Web工作目录: ``/var/www/html``
- phpinfo路径: ``/var/www/html/info.php``

重启
~~~~~~~~~~~~~~~~

.. code-block:: bash

   # php5
   $ sudo service php5-fpm restart

   # php7
   $ sudo service php7.0-fpm restart

   # nginx
   $ sudo service nginx restart

基础的Django Web服务器
----------------------------------------------------------

介绍
~~~~~~~~~~~~~~~~

Django + Mysql

.. code-block:: bash
   
   -s django -p project_name 或者 --server django --project project_name

.. note:: 如果使用 ``-p project_name`` 参数，则会创建一个以 ``project_name`` 为名字的文件夹，并将Django项目放置在该文件夹下面，否则默认使用 ``demo`` 作为文件夹名。


默认的配置信息
~~~~~~~~~~~~~~~

- Mysql密码: ``password``
- 项目路径: ``/var/www/html/project_name``
- Python虚拟环境路径: ``~/.project_name``

Django的Mysql配置
~~~~~~~~~~~~~~~~~~~
默认安装完成后,Django使用的数据库是Sqlite3,我们需要将其修改成为Mysql

- 编辑``/var/www/html/project_name/project_name/settings.py``

.. code-block:: bash
   
   $ cd /var/www/html/project_name/project_name
   $ vim settings.py

- 修改数据库配置为Mysql

.. code-block:: bash
   
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'HOST': 'localhost',
           'NAME' : 'your_database_name',
           'USER' : 'root',
           'PASSWORD' : 'password'
       }
   }

- 激活Django项目的虚拟环境

.. code-block:: bash
   
   $ source ~/.project_name/bin/activate 

- 进入 ``/var/www/html/project_name`` 目录并执行数据库迁移

.. code-block:: bash
   
   $ cd /var/www/html/project_name
   $ python manage.py migrate 



高级的Django Web服务器
----------------------------------------------------------

介绍
~~~~~~~~~~~~~~~~

Django + Uwsgi + Nginx + Supervisor

.. code-block:: bash
   
   -s django-uwsgi -p project_name 或者 --server django-uwsgi --project project_name

默认的配置信息
~~~~~~~~~~~~~~~

基本配置：

- 项目目录: ``/var/www/html/project_name``
- python虚拟环境: ``~/.project_name``
- Mysql密码: ``password``

服务器配置：

- nginx配置文件路径: ``/etc/nginx/sites-enabled/default``
- uwsgi配置文件路径: ``/var/www/html/project_name/project_name.ini``
- supervisor配置文件路径: ``/etc/supervisor/conf.d/project_name_sysd.conf``

日志配置：

- django基本输出日志: ``/var/log/project_name_out.log``
- django错误信息日志: ``/var/log/project_name_error.log``

重启
~~~~~~~~~

.. code-block:: bash
   
   # nginx服务器重启
   $ service nginx restart

   # uwsgi服务器重启
   $ sudo supervisorctl restart project_name

   # 启动uwsgi服务
   $ sudo supervisorctl start project_name

   # 重加载supervisor配置文件
   $ sudo supervisorctl reread
   $ sudo supervisorctl update

设置supervisor默认启动

.. code-block:: bash

   # 针对ubuntu 16，supervisor重启后自动运行
   $ sudo systemctl enable supervisor
   $ sudo systemctl start supervisor

   # 针对ubuntu 14
   $ sudo update-rc.d supervisor enable