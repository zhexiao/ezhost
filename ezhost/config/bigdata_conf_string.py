kafka_home = '/opt/kafka'
kafka_download_url = "http://mirrors.tuna.tsinghua.edu.cn/apache/kafka/0.10.2.0/kafka_2.10-0.10.2.0.tgz"

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
