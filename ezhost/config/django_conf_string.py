supervisor_dir = '/etc/supervisor'
supervisor_conf_dir = '{0}/conf.d'.format(supervisor_dir)

uwsgi_ini_conf = """[uwsgi]
chdir = {0}/{1}
home = {2}
module = {1}.wsgi:application

uid = {3}
gid = www-data

master = true
processes = 5

socket = /tmp/{1}.sock
chmod-socket = 664
vacuum = true
"""

uwsgi_nginx_conf = """server {{
    listen 80;
    server_name localhost;

    location = /favicon.ico {{
        access_log off;
        log_not_found off;
    }}

    location / {{
        include uwsgi_params;
        uwsgi_pass unix:/tmp/{0}.sock;
    }}
}}
"""

uwsgi_supervisor_conf = """[program:{0}]
command=uwsgi --ini {1}/{0}.ini
directory={1}
numprocs=1
stdout_logfile=/var/log/{0}_out.log
stderr_logfile=/var/log/{0}_error.log
autostart=true
autorestart=true
startsecs=2
stopwaitsecs=2
killasgroup=true
priority=998
"""
