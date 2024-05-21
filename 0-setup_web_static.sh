#!/usr/bin/env bash
# Sets up a web servers for the deployment of web_static
sudo apt update
sudo apt install nginx -y
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html
echo 'We are live' | sudo tee /data/web_static/releases/test/index.html
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i 's|server_name _;|server_name _;\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}|g' /etc/nginx/sites-enables/default
