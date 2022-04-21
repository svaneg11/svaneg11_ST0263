#!/bin/bash

cd backend
sudo apt update
sudo apt install -y nodejs npm
npm install
cd ..
sudo chmod 777 ./../get-docker.sh
./../get-docker.sh
cd backend-2
docker-compose up -d