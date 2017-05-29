FROM node:slim
MAINTAINER Allan Berry "allan.berry@gmail.com"
WORKDIR /static
VOLUME /static
RUN npm install -g node-static

EXPOSE 80

CMD static --host-address 0.0.0.0 -p 80 --gzip
