#!/bin/bash

mysqldump {{ mysql_database }} > /home/backup/backup/{{ mysql_database}}.dump