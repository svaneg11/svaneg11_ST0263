#!/bin/bash

cd frontend
sudo apt update
sudo apt install -y nodejs npm
npm install
cd ..
sudo chmod 777 ./../get-docker.sh
./../get-docker.sh
docker-compose up -d