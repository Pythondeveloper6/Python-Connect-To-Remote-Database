#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb as db


## infor for connecting
HOST = "  "       ## SERVER IP ADDRESS
PORT =            ## PORT NUMBER
USER = " "        ## DATABASE USERNAME
PASSWORD = "  "   ## DATABASE PASSWORD
DB = "  "         ## DATABASE NAME


## connection statement
connection = db.connect(host=HOST, port=PORT,user=USER, passwd=PASSWORD, db=DB)

print('connected')
cur = connection.cursor()

## retrieving information from names table
cur.execute("SELECT * from names")
result = cur.fetchall()
for item in result:
    print(item)



