#!/bin/bash

cd backend
sudo apt update
sudo apt install -y nodejs npm
npm install
cd ..
sudo chmod 777 ./../get-docker.sh
./../get-docker.sh
export URL_DB_CONNECTION=mongodb://10.128.0.14/bookstore-production
docker-compose up -d