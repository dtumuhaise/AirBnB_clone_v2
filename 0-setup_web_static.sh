#!/usr/bin/env bash
# setup web sercer for deployment of web_static

sudo apt-get update
sudo apt-get insall nginx -y

sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

echo "<h1>hello World</h1>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sfn /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '$ a location /hbnb_static/ { \n alias /data/web_static/current/; \n }' /etc/nginx/sites-available/default
sudo service nginx restart