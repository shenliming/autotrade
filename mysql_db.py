#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""Mysql DB Module"""

import MySQLdb

class MySql(object):
    def __init__(self, host, user, pwd, charset):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.charset = charset
        pass
    def excute_sql(self, sql):
        try:
            self.db.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
        self.db.close()

    def connect_db(self):
        self.db = MySQLdb.connect(self.host, self.user, self.pwd, self.charset)

    def create_db(self, db_name):
        self.connect_db()
        sql = 'create database if not exists ' + db_name
        self.excute_sql(sql)

    def create_table(self, table_name):
        """create table"""
        pass
