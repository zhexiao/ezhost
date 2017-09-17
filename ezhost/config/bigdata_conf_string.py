global_env_home = '/etc/environment'
project_root = '/opt'

kafka_home = '{0}/kafka'.format(project_root)
kafka_download_url = "http://mirrors.tuna.tsinghua.edu.cn/apache/kafka/0.10.2.0/kafka_2.10-0.10.2.0.tgz"

spark_home = '{0}/spark'.format(project_root)
hadoop_home = '{0}/hadoop'.format(project_root)
spark_download_url = "http://mirrors.tuna.tsinghua.edu.cn/apache/spark/spark-2.2.0/spark-2.2.0-bin-hadoop2.7.tgz"
hadoop_download_url = "http://mirror.bit.edu.cn/apache/hadoop/common/hadoop-2.7.4/hadoop-2.7.4-src.tar.gz"

elastic_download_url = "https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.5.0.deb"
logstash_download_url = "https://artifacts.elastic.co/downloads/logstash/logstash-5.5.0.deb"
kibana_download_url = "https://artifacts.elastic.co/downloads/kibana/kibana-5.5.0-amd64.deb"


systemctl_config = """
[Unit]
Description={service_name}
After=syslog.target network.target remote-fs.target nss-lookup.target

[Service]
Type=simple
ExecStart={start_cmd}
ExecStop={stop_cmd}
PrivateTmp=true

[Install]
WantedBy=multi-user.target 
"""

spark_env = """
export SPARK_HOME={spark_home}
export HADOOP_HOME={hadoop_home}
export PATH=$PATH:$JAVA_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$SCALA_HOME/bin
export SPARK_LIBARY_PATH=.:$JAVA_HOME/lib:$JAVA_HOME/jre/lib:$HADOOP_HOME/lib/native

export SPARK_MASTER_HOST={host}

SPARK_LOCAL_DIRS={spark_home}
SPARK_WORKER_MEMORY={SPARK_WORKER_MEMORY}
"""

ubuntu_source_list_16 = """
deb http://mirrors.aliyun.com/ubuntu/ xenial main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-proposed main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ xenial main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse
"""