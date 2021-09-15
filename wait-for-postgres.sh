#!/bin/bash
Red='\e[31m'

export WAIT_HOSTS="$POSTGRES_HOST:$POSTGRES_PORT"
export WAIT_HOSTS_TIMEOUT=300
export WAIT_SLEEP_INTERVAL=30
export WAIT_HOST_CONNECT_TIMEOUT=30
printf $Red"Waiting for $WAIT_HOSTS ...\n"
/wait