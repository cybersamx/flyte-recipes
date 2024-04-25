FROM python:3.12.3-bullseye

RUN set -ex; \
    apt-get -y update; \
    apt-get install -y --no-install-recommends \
            awscli \
            curl \
            dnsutils \
            iputils-ping \
            jq \
            netcat \
            openssl \
            postgresql-client \
            telnet \
            vim

RUN mkdir -p /root/.aws

WORKDIR /root/.aws
COPY src/aws-config ./config
COPY src/aws-credentials ./config

WORKDIR /root
CMD ["/bin/bash"]
