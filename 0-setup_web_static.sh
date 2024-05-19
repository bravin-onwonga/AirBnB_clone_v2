#!/usr/bin/env bash
# Sets up a web servers for the deployment of web_static
sudo apt update
sudo apt install nginx -y
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo 'We are live' > /data/web_static/releases/test/index.html
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chwon -R ubuntu:ubuntu /data/
