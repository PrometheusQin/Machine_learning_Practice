# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 23:44:47 2018

@author: Flame

使用不了谷歌服务，可以换用ditu.google.cn
"""
import requests

def Geocoding(address):
    lat = 0
    lng = 0
    
    #url='https://ditu.google.cn/maps/api/geocode/json?'
    url='https://maps.googleapis.com/maps/api/geocode/json?'
    Data = {'address': address,
             'key':'AIzaSyAuoBs13cTNJezzpJ6NWVPQJFQ5IK6q19E'}
    r = requests.get(url, params=Data)
    r.encoding = r.apparent_encoding
    if r.json()['status']=='OK':
        #r.json()['results'][0]['address_components']  
        #9 编号-街道-行政社区-区域-县-州-国家-邮编-邮政编码后缀
        #r.json()['results'][0]['formatted_address']详细地址
        lat = r.json()['results'][0]['geometry']['location']['lat']
        lng = r.json()['results'][0]['geometry']['location']['lng']
    else:
        print('status error')
    return lat,lng
    
if __name__ == '__main__': 
    #address='10860 SW Beaverton-Hillsdale Hwy	Beaverton, OR'
    address = '河南省鹿邑县高集乡'
    lat,lng = Geocoding(address)
    print(address)
    print('lat:',lat,'\nlng:',lng)