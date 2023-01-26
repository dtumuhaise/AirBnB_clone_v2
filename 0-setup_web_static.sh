#!/usr/bin/env bash
# setup web sercer for deployment of web_static

sudo apt-get update
sudo apt-get insall nginx -y
sudo mkdir /data/
sudo mkdir /data/web_static/
sudo mkdir /data/web_static/releases/
sudo mkdir /data/web_static/shared/
sudo mkdir /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
html_content="<h1>hello World</h1>"
echo "$html_content" >> index.html
sudo ln -sfn /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo service nginx restart
