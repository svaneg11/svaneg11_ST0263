#!/bin/bash

sudo apt-get update
sudo apt-get install -y nginx
sudo apt update
sudo apt install -y snapd
sudo snap install core; sudo snap refresh core
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
sudo certbot --nginx certonly -d www.svaneg11-lab2-distribuido.tk -d svaneg11-lab2-distribuido.tk
mkdir -p ssl
sudo cp /etc/letsencrypt/live/www.svaneg11-lab2-distribuido.tk/* /home/svaneg11/svaneg11_ST0263/U2-Lab2/distribuido/nginx-front/ssl
sudo apt-get install psmisc
sudo fuser -k 80/tcp
sudo chmod 777 ./../get-docker.sh
./../get-docker.sh
docker-compose up --build -d