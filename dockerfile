FROM node:10

WORKDIR /usr/src/app

COPY . ./

EXPOSE 6000

CMD [ "npm", "start"]