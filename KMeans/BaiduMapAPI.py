# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 20:57:23 2018

@author: Flame

inference：https://zhuanlan.zhihu.com/p/25845538
intro：仅适用于国内地址查询经纬度，国外无结果
"""


import json
from urllib.request import urlopen, quote

def getlnglat(address):
    url = 'http://api.map.baidu.com/geocoder/v2/'
    output = 'json'
    ak = 'Nq6xvK1GGytlV5jsztOnIxK3RhC7823N'
    add = quote(address) #由于本文城市变量为中文，为防止乱码，先用quote进行编码
    uri = url + '?address=' + add  + '&output=' + output + '&ak=' + ak
    req = urlopen(uri)
    res = req.read().decode() #将其他编码的字符串解码成unicode
    temp = json.loads(res) #对json数据进行解析
    lat = temp['result']['location']['lat']
    lng = temp['result']['location']['lng']
    return lat,lng

address = '河南省鹿邑县高集乡王屯行政村'
#address = '10860 SW Beaverton-Hillsdale Hwy	Beaverton' 
# 查询国外信息结果：
#temp:{'msg': 'Internal Service Error:无相关结果', 
#      'results': [], 'status': 1}
lat,lng=getlnglat(address)
print(address)
print('lat:', lat, '\nlng:', lng)


