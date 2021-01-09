FROM node:alpine
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app

RUN npm i

ENV SASS_PATH=./node_modules
# RUN npm install node-sass
RUN npm install node-sass@4.14.1
EXPOSE 3000
CMD [ "npm", "start" ]
