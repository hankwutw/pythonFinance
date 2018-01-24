# coding: utf-8

import urllib2
import json
import sys,csv,re
import datetime
from time import sleep
import time

def getStatis():
    ts =  int(time.time() * 1000 + 1000)
    url = 'http://mis.twse.com.tw/stock/api/getStatis.jsp?ex=tse&delay=0&_='+str(ts)
    print url
    response = urllib2.urlopen(url)
    d = response.read()
    data = json.loads(d) 
    if data["rtmessage"]=="OK":
        return data["detail"]
    else:
        return "noData"
    
def getStockInfo():
    ts =  int(time.time() * 1000 + 1000)
    url='http://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch=tse_t00.tw&json=1&delay=0&_='+str(ts)
    print url
    response = urllib2.urlopen(url)
    d = response.read()
    data = json.loads(d) 
    if data["rtmessage"]=="OK":
        return data["msgArray"][0]
    else:
        return "noData"
while getStockInfo()['t'] <>"13:31:00":
    detail = getStatis()
    stockInfo=getStockInfo()
    sysDate=stockInfo['d']
    index=stockInfo['z']
    twOpen=stockInfo['o']
    twTime=stockInfo['t']
    twClose=stockInfo['y']
    print sysDate,index,twOpen,twTime,float(index)-float(twOpen),float(index)-float(twClose)
    sleep(30)
#整體市場成交金額 tz,股票fz,基金sz,認購權證	cz,認售權證bz
#整體市場成交數量 tv,股票fv,基金sv,認購權證	cv,認售權證bv
#整體市場成交筆數 tr,股票fr,基金sr,認購權證	cr,認售權證br
#while getStatis <>"noData":
#    detail=getStatis
#    print 
#    sleep(30)


# In[ ]:

1513648392925

