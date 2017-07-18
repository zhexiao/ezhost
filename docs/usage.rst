使用方法
===============

Ezhost主要是用于主机与客户机通信执行自动化安装，在主机上执行一系列的安装命令来控制客户机。

使用客户机的用户名与密码进行连接
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   $ ezhost -H host -U user -P password [keyword]

使用客户机的用户名与SSH KEY进行连接
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   $ ezhost -H host -U user -K ~/.ssh/keyfile.pem [keyword]

使用客户机的配置文件进行连接
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

在/config/文件夹下面创建 **ezhost.ini** 的配置文件，然后在此配置文件中写入如下配置：

.. code-block:: bash
   :linenos:

   [develop_server]
   host=hostd
   user=userd
   passwd=passwordd

   [test_server]
   host=hostt
   user=usert
   keyfile=~/.ssh/keyfile.pem


.. note:: 如果你不想暴露你的客户机密码，则可以使用SSH KEY代替密码。将 ``passwd=password`` 改成 ``keyfile=~/.ssh/keyfile.pem`` 即可.（此处假设你的SSH KEY文件保存在~/.ssh/keyfile.pem里面）

当你的配置文件创建完成后，可以使用如下命令访问到客户机：

.. code-block:: bash

   $ ezhost -C /config/ezhost.ini develop_server [keyword]


[keyword]的使用方法
~~~~~~~~~~~~~~~~~~~~~~~

[keyword]是一系列的，已存在于Ezhost里面的服务器替代名，例如这里安装LAMP服务器，我们就把[keyword]替换成了 `-s lamp`。

.. code-block:: bash

   $ ezhost -C development.ini -s lamp

参数解释
~~~~~~~~~~~~~~~~~~~~~~~

.. glossary::

   -H 客户机地址
   -U 客户机用户名
   -P 客户机密码
   -K 客户机SSH KEY路径
   -C 配置文件路径