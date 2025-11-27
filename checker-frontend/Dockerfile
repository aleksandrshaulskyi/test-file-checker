FROM node:20-alpine AS build

WORKDIR /checker-frontend

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build