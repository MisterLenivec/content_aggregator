FROM node:15.5.0

WORKDIR /frontend

ENV PATH /frontend/node_modules/.bin:$PATH

COPY package.json /frontend/package.json
RUN npm install

COPY . /frontend

CMD npm run serve
