#!/usr/bin/env bash
set -e
STREAMS_FILE_PATH=${STREAMS_FILE_PATH:-streams.json}
SERVER_CONFIG_PATH=${SERVER_CONFIG_PATH:-server.json}
STATSERVE_SERVER_PORT=${STATSERVE_SERVER_PORT:-9001}
LOG_LEVEL=${LOG_LEVEL:-"info"}

STATSERVE_OPTS="--streams-filepath ${STREAMS_FILE_PATH} --server-config-filepath ${SERVER_CONFIG_PATH} --log-level ${LOG_LEVEL}"

statserve-server ${STATSERVE_OPTS}