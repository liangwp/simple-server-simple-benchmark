FROM rust:1.65-bullseye

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update -y \
    && apt install -y \
        dumb-init=1.2.5-1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace
RUN mkdir -p src

COPY ./Cargo.* /workspace/
COPY ./src/* /workspace/src

RUN cargo build --release

ENTRYPOINT [ "dumb-init", "--" ]
