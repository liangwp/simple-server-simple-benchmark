FROM node:18.12-bullseye

ENV NODE_ENV=production
ARG DEBIAN_FRONTEND=noninteractive

RUN apt update -y \
    && apt install -y \
        dumb-init=1.2.5-1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

RUN npm init -y \
    && npm install --save \
        express@4.18.2

RUN mkdir -p /workspace/src
COPY ./src/* /workspace/src/

ENTRYPOINT [ "dumb-init", "--" ]
