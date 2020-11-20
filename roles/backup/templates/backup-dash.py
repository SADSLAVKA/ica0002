#!/usr/bin/python3

import os
import sqlite3

conn = sqlite3.connect("/var/lib/grafana/grafana.db")
title_list = conn.execute("select title from dashboard;").fetchall()
path = "/home/backup/backup/dashboards"
if (not os.path.isdir(path)):
    os.mkdir(path, 0o744)
for row in title_list:
    json = conn.execute(f"select data from dashboard where title = '{row[0]}'").fetchone()[0]
    if (type(json) == bytes): # it can be str, it can be bytes idk
        json = json.decode("utf-8")
    filename = row[0].lower().replace(' ', '_') + ".json"
    f = open(f"{path}/{filename}", "w")
    f.write(json)
    #print(f"Wrote dashboard '{row[0]}' to /home/backup/backup/{filename}")
    f.close()
conn.close()