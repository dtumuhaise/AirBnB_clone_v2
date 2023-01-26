#!/usr/bin/env bash
# setup web sercer for deployment of web_static

sudo apt-get update
sudo apt-get insall nginx -y

sudo mkdir /data/web_static/releases/
sudo mkdir /data/web_static/shared/
sudo mkdir /data/web_static/releases/test/

sudo echo "<h1>hello World</h1>" >> /data/web_static/releases/test/index.html

sudo ln -sfn /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo echo "location /hbnb_static/ {
    alias /data/web_static/current/;
    }" >> /etc/nginx/sites-available/default

sudo service nginx restart
