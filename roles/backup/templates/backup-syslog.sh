#!/bin/bash

influx -database telegraf -precision rfc3339 \
-execute "select timestamp, hostname, appname, message from syslog where time >= now() - 1d;" \
> /home/backup/backup/logs.txt
