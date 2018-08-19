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
        
    def excute_sql(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
            print "SQL execute ok"
        except Exception, e:
            print e
            self.db.rollback()
            print "DB roll back"
        self.db.close()

    def connect_db(self):
        self.db = MySQLdb.connect(self.host, self.user, self.pwd, db='test')
        self.cursor = self.db.cursor()
        print self.cursor

    def create_table(self, table_name):
        """create table"""
        self.connect_db()
        sql = 'CREATE TABLE ' + table_name
        sql += """ (
        FIRST_NAME  CHAR(20) NOT NULL,
        LAST_NAME  CHAR(20),
        AGE INT,  
        SEX CHAR(1),
        INCOME FLOAT
        ) """
        self.excute_sql(sql)