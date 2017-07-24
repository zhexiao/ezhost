大数据应用列表（运行在Ubuntu 16）
===================================

Kafka
------
Kafka是一种高吞吐量的分布式发布订阅消息系统，它可以处理所有的动作流数据。
它通过O(1)的磁盘数据结构提供消息的持久化，这种结构对于即使数以TB的消息存储也能够保持长时间的稳定性能。
拥有高吞吐量即使是非常普通的硬件，Kafka也可以支持每秒数百万的消息。
同时Kafka支持通过服务器和消费机集群来分区消息。

安装关键字
~~~~~~~~~~~~
.. code-block:: bash

    -s bigdata -ba kafka 或者 --server bigdata --bigdata-app kafka


话题（topic）
~~~~~~~~~~~~~~
.. code-block:: bash

    # 创建话题
    sudo ./bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test

    # 检查话题
    sudo ./bin/kafka-topics.sh --list --zookeeper localhost:2181

    # 删除话题
    sudo ./bin/kafka-topics.sh --zookeeper localhost:2181 --delete --topic test

运行生产者（producer）
~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: bash

    sudo ./bin/kafka-console-producer.sh --broker-list <IP Address>:9092 --topic test

运行消费者（consumer）
~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: bash

    sudo ./bin/kafka-console-consumer.sh --bootstrap-server <IP Address>:9092 --topic test --from-beginning

Kafka安装配置
~~~~~~~~~~~~~~~~~
- 安装路径：/opt/kafka
- bin目录: /opt/kafka/bin
- zookeeper配置文件：/opt/kafka/config/zookeeper.properties
- kafka配置文件：/opt/kafka/config/server.properties

服务
~~~~~~~
.. code-block:: bash

    # 查看状态
    sudo systemctl status kafka
    sudo systemctl status zookeeper

    # 重启服务
    sudo systemctl restart kafka
    sudo systemctl restart zookeeper


Spark
--------
Spark 是专为大规模数据处理而设计的快速通用的计算引擎。Spark 是一种与 Hadoop 相似的
开源集群计算环境，但是两者之间还存在一些不同之处，这些有用的不同之处使 Spark 在某些
工作负载方面表现得更加优越，换句话说，Spark 启用了内存分布数据集，除了能够提供交互式查询外，
它还可以优化迭代工作负载。

安装关键字
~~~~~~~~~~
.. code-block:: bash

    -s bigdata -ba spark 或者 --server bigdata --bigdata-app spark

安装配置
~~~~~~~~~~~~~
Spark
^^^^^^^^
- 安装路径：/opt/spark
- 配置路径：/opt/spark/conf

Hadoop
^^^^^^^^
- 安装路径：/opt/hadoop
- 配置路径：/opt/hadoop/etc

测试
~~~~~~
.. code-block:: bash

    cd /opt/spark
    ./bin/run-example SparkPi 10




Spark Cluster
-------------------

demo_config.ini
~~~~~~~~~~~~~~~~~
.. code-block:: bash

    [demo_spark_master]
    host=192.168.33.25
    user=ubuntu
    passwd=18fc2f8e53c021a965cd9628
    SPARK_DRIVER_MEMORY=512M

    [demo_spark_slave1]
    host=192.168.33.26
    user=ubuntu
    passwd=18fc2f8e53c021a965cd9628

    [demo_spark_slave2]
    host=192.168.33.27
    user=ubuntu
    passwd=18fc2f8e53c021a965cd9628

.. note::

    可以在Spark主（master）服务器中配置每个从（slave）服务器的执行内存大小，
    通过 **SPARK_DRIVER_MEMORY** 进行赋值。


安装实例
~~~~~~~~~~~
我们把 **demo_config.ini** 中的 **demo_spark_master** 做为spark主（master）服务器,
把 **demo_spark_slave1** 作为第一个从（slave）服务器，则安装命令如下：

.. code-block:: bash

    ezhost -C /vagrant/ezhost/data/demo_config.ini demo_spark_master -s bigdata -ba spark -add-slave demo_spark_slave1


假如你已经完成了上面的命令操作，现在想为 **demo_spark_master** 主服务器多增加一个从服务器
**demo_spark_slave2** ，则可以通过增加 *-skip-master* 来避免重复安装主服务器，安装命令如下：

.. code-block:: bash

    ezhost -C /vagrant/ezhost/data/demo_config.ini demo_spark_master -s bigdata -ba spark -add-slave demo_spark_slave2 -skip-master


Web UI
~~~~~~~~~~~~~~~
.. code-block:: bash

    192.168.33.25:8080



Elasticsearch
----------------
Elasticsearch是个开源分布式搜索引擎，它的特点有：分布式，零配置，自动发现，索引自动分片，
索引副本机制，restful风格接口，多数据源，自动搜索负载等。

安装关键字
~~~~~~~~~~
.. code-block:: bash

    -s bigdata -ba elastic 或者 --server bigdata --bigdata-app elastic

安装配置
~~~~~~~~~~~~~
- 安装路径：/usr/share/elasticsearch
- 配置路径：/etc/default/elasticsearch

测试
~~~~~~~
.. code-block:: bash

    curl 127.0.0.1:9200

服务
~~~~~~
.. code-block:: bash

    # 查看状态
    sudo systemctl status elasticsearch

    # 重启服务
    sudo systemctl restart elasticsearch



Logstash
-----------
Logstash是一个完全开源的工具，他可以对你的日志进行收集、过滤，并将其存储供以后使用。

安装关键字
~~~~~~~~~~~~
.. code-block:: bash

    -s bigdata -ba logstash 或者 --server bigdata --bigdata-app logstash

安装配置
~~~~~~~~~~~~~
- 安装路径：/usr/share/logstash
- 配置路径：/etc/logstash

服务
~~~~~~
.. code-block:: bash

    # 查看状态
    sudo systemctl status logstash

    # 重启服务
    sudo systemctl restart logstash



Kibana
------
Kibana也是一个开源和免费的工具，它可以为Logstash和ElasticSearch提供的日志分析友好的Web界面，
可以帮助您汇总、分析和搜索重要数据日志。

安装关键字
~~~~~~~~~~
.. code-block:: bash

    -s bigdata -ba kibana 或者 --server bigdata --bigdata-app kibana

安装配置
~~~~~~~~~~~~~
- 安装路径：/usr/share/kibana
- 配置路径：/etc/kibana

测试
~~~~~~~~~~~~
访问web页面：http://<IP Address>:5601

服务
~~~~~~
.. code-block:: bash

    # 查看状态
    sudo systemctl status kibana

    # 重启服务
    sudo systemctl restart kibana
