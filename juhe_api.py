#!/usr/bin/python
# -*- coding: utf-8 -*-
import json, urllib
from urllib import urlencode
from enum import Enum
#----------------------------------
# 股票数据调用示例代码 － 聚合数据
# 在线接口文档：http://www.juhe.cn/docs/21
#----------------------------------

class Market(Enum):
    sh = 1
    sz = 2
    hk = 3
    us = 4

class Juhe(object):

    def __init__(self):
        #配置您申请的APPKey
        self.appkey = "57fc3d28c7b8b66a9579e384e650056c"
        self.itemsEachPage = 20

    #沪深股市
    def getStockData(self, stock_code, m="GET"):
        url = "http://web.juhe.cn:8080/finance/stock/hs"
        params = {
            "gid" : stock_code, #股票编号，上海股市以sh开头，深圳股市以sz开头如：sh601009
            "key" : self.appkey, #APP Key
    
        }
        params = urlencode(params)
        if m =="GET":
            f = urllib.urlopen("%s?%s" % (url, params))
        else:
            f = urllib.urlopen(url, params)
    
        content = f.read()
        res = json.loads(content)
        if res:
            error_code = res["error_code"]
            if error_code == 0:
                #成功请求
                print res["result"]
                return res
            else:
                print "%s:%s" % (res["error_code"],res["reason"])
        else:
            print "request api error"
    
    #香港股市
    def request2(self, m="GET"):
        url = "http://web.juhe.cn:8080/finance/stock/hk"
        params = {
            "num" : "", #股票代码，如：00001 为“长江实业”股票代码
            "key" : self.appkey, #APP Key
    
        }
        params = urlencode(params)
        if m =="GET":
            f = urllib.urlopen("%s?%s" % (url, params))
        else:
            f = urllib.urlopen(url, params)
    
        content = f.read()
        res = json.loads(content)
        if res:
            error_code = res["error_code"]
            if error_code == 0:
                #成功请求
                print res["result"]
                return res
            else:
                print "%s:%s" % (res["error_code"],res["reason"])
        else:
            print "request api error"
    
    #美国股市
    def request3(self, m="GET"):
        url = "http://web.juhe.cn:8080/finance/stock/usa"
        params = {
            "gid" : "", #股票代码，如：aapl 为“苹果公司”的股票代码
            "key" : self.appkey, #APP Key
    
        }
        params = urlencode(params)
        if m =="GET":
            f = urllib.urlopen("%s?%s" % (url, params))
        else:
            f = urllib.urlopen(url, params)
    
        content = f.read()
        res = json.loads(content)
        if res:
            error_code = res["error_code"]
            if error_code == 0:
                #成功请求
                print res["result"]
                return res
            else:
                print "%s:%s" % (res["error_code"],res["reason"])
        else:
            print "request api error"

    def _geteAllStocks(self, func):
        page = 1
        data = func(page)
        jsonData = json.loads(json.dumps(data))
        total = int(jsonData["result"]["totalCount"])
        ret = json.loads('{"totalCount":0, "data":[]}')
        ret["totalCount"] = total
        ret["data"] = jsonData["result"]["data"]
        numOfPage = total / self.itemsEachPage + ( 0 if total % self.itemsEachPage == 0 else 1 )
        while page < numOfPage:
            page += 1
            data = func(page)
            jsonData = json.loads(json.dumps(data))
            ret["data"].extend(jsonData["result"]["data"])
        return ret

    def getAlltocksByMarket(self, market):
        if market == Market.sh:
            return self._geteAllStocks(self.request7)
        elif market == Market.sz:
            return self._geteAllStocks(self.request6)

    #香港股市列表
    def request4(self, page, m="GET"):
        url = "http://web.juhe.cn:8080/finance/stock/hkall"
        params = {
            "key" : self.appkey, #您申请的APPKEY
            "page" : page, #第几页,每页20条数据,默认第1页
    
        }
        params = urlencode(params)
        if m =="GET":
            f = urllib.urlopen("%s?%s" % (url, params))
        else:
            f = urllib.urlopen(url, params)
    
        content = f.read()
        res = json.loads(content)
        if res:
            error_code = res["error_code"]
            if error_code == 0:
                #成功请求
                print res["result"]
                return res
            else:
                print "%s:%s" % (res["error_code"],res["reason"])
        else:
            print "request api error"
    
    #美国股市列表
    def request5(self, page, m="GET"):
        url = "http://web.juhe.cn:8080/finance/stock/usaall"
        params = {
            "key" : self.appkey, #您申请的APPKEY
            "page" : page, #第几页,每页20条数据,默认第1页
    
        }
        params = urlencode(params)
        if m =="GET":
            f = urllib.urlopen("%s?%s" % (url, params))
        else:
            f = urllib.urlopen(url, params)
    
        content = f.read()
        res = json.loads(content)
        if res:
            error_code = res["error_code"]
            if error_code == 0:
                #成功请求
                print res["result"]
                return res
            else:
                print "%s:%s" % (res["error_code"],res["reason"])
        else:
            print "request api error"

    #深圳股市列表
    def request6(self, page, m="GET"):
        url = "http://web.juhe.cn:8080/finance/stock/szall"
        params = {
            "key" : self.appkey, #您申请的APPKEY
            "page" : page, #第几页(每页20条数据),默认第1页
    
        }
        params = urlencode(params)
        if m =="GET":
            f = urllib.urlopen("%s?%s" % (url, params))
        else:
            f = urllib.urlopen(url, params)
    
        content = f.read()
        res = json.loads(content)
        if res:
            error_code = res["error_code"]
            if error_code == 0:
                #成功请求
                print res["result"]
                return res
            else:
                print "%s:%s" % (res["error_code"],res["reason"])
        else:
            print "request api error"
    
    #沪股列表
    def request7(self, page, m="GET"):
        url = "http://web.juhe.cn:8080/finance/stock/shall"
        params = {
            "key" : self.appkey, #您申请的APPKEY
            "page" : page, #第几页,每页20条数据,默认第1页
        }
        params = urlencode(params)
        if m =="GET":
            f = urllib.urlopen("%s?%s" % (url, params))
        else:
            f = urllib.urlopen(url, params)
    
        content = f.read()
        res = json.loads(content)
        if res:
            error_code = res["error_code"]
            if error_code == 0:
                #成功请求
                print res["result"]
                return res
            else:
                print "%s:%s" % (res["error_code"],res["reason"])
        else:
            print "request api error"