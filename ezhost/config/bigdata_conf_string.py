kafka_home = '/opt/kafka'
kafka_download_url = "http://mirrors.tuna.tsinghua.edu.cn/apache/kafka/0.10.2.0/kafka_2.10-0.10.2.0.tgz"

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
