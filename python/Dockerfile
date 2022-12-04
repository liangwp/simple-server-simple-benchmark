FROM python:3.11-bullseye

ENV PYTHONUNBUFFERED=1
ARG DEBIAN_FRONTEND=noninteractive

RUN apt update -y \
    && apt install -y \
        dumb-init=1.2.5-1 \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install \
        fastapi==0.88.0 \
        uvicorn[standard]==0.20.0

WORKDIR /workspace

RUN mkdir -p /workspace/src
COPY ./src/* /workspace/src/

ENTRYPOINT [ "dumb-init", "--" ]
