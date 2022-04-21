#!/bin/bash

sudo apt-get install psmisc
sudo fuser -k 80/tcp
sudo chmod 777 ./../get-docker.sh
./../get-docker.sh
docker-compose up --build -d