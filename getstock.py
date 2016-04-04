#!/usr/bin/python

import urllib2

def getCurStockInfo(stockId):
    url = "http://hq.sinajs.cn/list=" + stockId
    return urllib2.urlopen(url).read()


print getCurStockInfo("sh601006")
