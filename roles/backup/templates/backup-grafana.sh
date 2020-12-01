#!/bin/bash
mkdir -p /home/backup/backup/grafana
rm -rf /home/backup/backup/grafana/*
cp -r /opt/docker/grafana/* /home/backup/backup/grafana/

mkdir -p /home/backup/backup/grafana_docker
rm -rf /home/backup/backup/grafana_docker/*
cp -r /var/lib/grafana/* /home/backup/backup/grafana_docker/