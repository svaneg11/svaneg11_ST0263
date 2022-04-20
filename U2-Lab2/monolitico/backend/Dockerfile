FROM node:latest

USER node
WORKDIR /home/backend
RUN cd /home/backend
RUN npm install
ENV NODE_ENV=production
ENV URL_DB_CONNECTION=mongodb://localhost/bookstore-production