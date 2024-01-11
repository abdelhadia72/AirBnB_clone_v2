#!/usr/bin/env bash
# sets up your web servers 
# for the deployment of web_static

# install nginx 
apt-get update -y
apt-get install -y nginx

# touch index.html to dir if exest or not 
path="/data/web_static/releases/test/"
mkdir -p $path && touch $path/index.html

#!/bin/bash

echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
" | sudo tee /data/web_static/releases/test/index.html


# creat a new symblic link
ln -fs /data/web_static/current /data/web_static/releases/test/

# change ownership
sudo chown -R ubuntu:ubuntu /data/

# update the Nginx configuration
sudo sed -i '/location \/hbnb_static\//a \
    alias /data/web_static/current/;' /etc/nginx/sites-available/default


# restart nginx
sudo service nginx restart
