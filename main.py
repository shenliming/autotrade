#!/usr/bin/python
# -*- coding: UTF-8 -*-

import mysql_db
import juhe_api
import json
#db = mysql_db.MySql('localhost', 'root', '111111', 'utf-8')
#db.create_table("EMPLOYEE")

j = juhe_api.Juhe()
data = json.loads(json.dumps(j.getAlltocksByMarket(juhe_api.Market.sh)))
print data["totalCount"]
print data["data"]