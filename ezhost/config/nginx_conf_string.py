web_dir = '/var/www/html'
web_ssl_dir = '/etc/nginx/ssl'

simple_web_config = """server
{{
    listen 80 default_server;
    listen [::]:80 default_server;

    root {0};
    autoindex on;

    # Add index.php to the list if you are using PHP
    index index.php index.html index.htm index.nginx-debian.html;

    server_name localhost;

    # Don't log robots.txt or favicon.ico files
    location = /favicon.ico {{ log_not_found off; access_log off; }}
    location = /robots.txt  {{ access_log off; log_not_found off; }}

    # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
    location ~ \.php$ {{
       include snippets/fastcgi-php.conf;
       # With php5-fpm:
       fastcgi_pass unix:/var/run/php5-fpm.sock;
    }}
}}
"""

simple_php7_web_config = """server
{{
    listen 80 default_server;
    listen [::]:80 default_server;

    root {0};
    autoindex on;

    # Add index.php to the list if you are using PHP
    index index.php index.html index.htm index.nginx-debian.html;

    server_name localhost;

    # Don't log robots.txt or favicon.ico files
    location = /favicon.ico {{ log_not_found off; access_log off; }}
    location = /robots.txt  {{ access_log off; log_not_found off; }}

    # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
    location ~ \.php$ {{
       include snippets/fastcgi-php.conf;
       # With php7.0-fpm:
       fastcgi_pass unix:/var/run/php/php7.0-fpm.sock;
    }}
}}
"""

simple_ssl_web_conf = """server
{{
    listen 443 default_server;
    listen [::]:443 default_server;

    root {dt[0]};
    autoindex on;

    # Add index.php to the list if you are using PHP
    index index.php index.html index.htm index.nginx-debian.html;

    server_name localhost;

    # Don't log robots.txt or favicon.ico files
    location = /favicon.ico {{ log_not_found off; access_log off; }}
    location = /robots.txt  {{ access_log off; log_not_found off; }}

    ssl on;
    ssl_certificate {dt[1]}/cert.pem;
    ssl_certificate_key {dt[1]}/cert.key;

    # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
    location ~ \.php$ {{
       include snippets/fastcgi-php.conf;
       # With php5-fpm:
       fastcgi_pass unix:/var/run/php5-fpm.sock;
    }}
}}
"""

wordpress_web_conf = """server
{{
    listen 80 default_server;
    listen [::]:80 default_server;

    root {0}/{1};
    autoindex on;

    # Add index.php to the list if you are using PHP
    index index.php index.html index.htm index.nginx-debian.html;

    server_name localhost;
    location / {{
        try_files $uri $uri/ /index.php?q=$uri&$args;
    }}

    # Don't log robots.txt or favicon.ico files
    location = /favicon.ico {{ log_not_found off; access_log off; }}
    location = /robots.txt  {{ access_log off; log_not_found off; }}

    # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
    location ~ \.php$ {{
       include snippets/fastcgi-php.conf;
       # With php5-fpm:
       fastcgi_pass unix:/var/run/php5-fpm.sock;
       fastcgi_split_path_info ^(.+\.php)(/.+)$;
    }}
}}
"""

wordpress_php7_web_conf = """server
{{
    listen 80 default_server;
    listen [::]:80 default_server;

    root {0}/{1};
    autoindex on;

    # Add index.php to the list if you are using PHP
    index index.php index.html index.htm index.nginx-debian.html;

    server_name localhost;
    location / {{
        try_files $uri $uri/ /index.php?q=$uri&$args;
    }}

    # Don't log robots.txt or favicon.ico files
    location = /favicon.ico {{ log_not_found off; access_log off; }}
    location = /robots.txt  {{ access_log off; log_not_found off; }}

    # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
    location ~ \.php$ {{
       include snippets/fastcgi-php.conf;
       # With php7-fpm:
       fastcgi_pass unix:/var/run/php/php7.0-fpm.sock;
       fastcgi_split_path_info ^(.+\.php)(/.+)$;
    }}
}}
"""
