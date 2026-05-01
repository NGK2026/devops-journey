FROM node:22-slim

ENV MONGO_DB_USERNAME=admin \
    MONGO_DB_PASSWORD=password

# RUN mkdir -p /home/app.. setting WORKDIR automatically creates it
WORKDIR /home/app

COPY ./app /home/app

CMD ["node", "server.js"]