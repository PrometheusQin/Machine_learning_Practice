# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 17:39:18 2018

@author: Flame
"""
# 无网络google连不上，使用method 1
# 中英文都可以使用，很方便，并且国内外均可查找，查找国内时小地点查不到
import urllib
from urllib.request import urlopen  
import json  
  
def getGeoForAddress(address):
    addressQuote = urllib.parse.quote(address, ':?=/')
    
    #method 1：使用http://ditu.google.cn/maps/api/geocode/json?网站--google地图不能使用时 
    #addressUrlQuote = "http://ditu.google.cn/maps/api/geocode/json?address=" + addressQuote
    
    #method 2：使用google地图API
    addressUrlQuote = "https://maps.googleapis.com/maps/api/geocode/json?address="+addressQuote+"&key=AIzaSyAuoBs13cTNJezzpJ6NWVPQJFQ5IK6q19E"
    
    
    print(addressUrlQuote)
    response = urlopen(addressUrlQuote).read().decode('utf-8') 
    responseJson = json.loads(response)  
    #type of response is string  
    # print(type(response))  
    #type of responseJson is dict  
    # print(type(responseJson))  
    #r=responseJson.get('results')
    #print(r)
    #print(type(r),len(r))
    lat = responseJson.get('results')[0]['geometry']['location']['lat']  
    lng = responseJson.get('results')[0]['geometry']['location']['lng']  
    print(address + '的经纬度是: %f, %f'  %(lat, lng))  
    #return [lat, lng]  
  
if __name__ == '__main__':
    address = '河南省鹿邑县高集乡'
    #address = "中国上海市中山北一路121号"
    address = '10860 SW Beaverton-Hillsdale Hwy Beaverton, OR'
    #北京市海淀区上地十街10号
    getGeoForAddress(address)
    

    
