#!/usr/bin/env bash
# Sets up a web servers for the deployment of web_static
sudo apt update
sudo apt install nginx -y
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo 'We are live' | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i 's|server_name 100.25.141.192;|server_name 100.25.141.192;\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n|g' /etc/nginx/sites-enabled/default
sudo service nginx restart
