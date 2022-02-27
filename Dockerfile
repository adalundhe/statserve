FROM python:3.8.6-slim
ENV PYTHONUNBUFFERED=0
ENV GRPC_DNS_RESOLVER=native
ARG PIP_INDEX_URL

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git gcc openssh-server sudo \
    apt-transport-https gnupg2 curl\
    python3-dev build-essential nginx libpq-dev \
    && apt-get clean

RUN mkdir /data

RUN pip install -i $PIP_INDEX_URL statserve

COPY scripts/* /
COPY config/nginx/* /etc/nginx/

EXPOSE 6669 6670 6671 9001 9002
RUN ["chmod", "+x", "/statserve_entrypoint.sh"]


ENTRYPOINT ["/statserve_entrypoint.sh"]

