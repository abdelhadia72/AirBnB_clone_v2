#!/usr/bin/env bash
# sets up your web servers 
# for the deployment of web_static

# install nginx 
apt-get update -y
apt-get install -y nginx

# touch index.html to dir if exest or not 
path="/data/web_static/releases/test/"
mkdir -p $path && touch $path/index.html

# creat a new symblic link
ln -s /data/web_static/current /data/web_static/releases/test/

# change ownership
sudo chown -R ubuntu:ubuntu /data/

# update the Nginx configuration
sudo bash -c "cat > /etc/nginx/sites-available/default" <<EOF
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=fx2Z5ZD_Rbo;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}
EOF

sudo service nginx restart
