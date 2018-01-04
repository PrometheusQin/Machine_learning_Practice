# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 00:46:19 2018

@author: Flame
"""

import requests

def Geocoding(address):
    lat = 0
    lng = 0
    url='http://api.map.baidu.com/geocoder/v2/?'
    Data = {'output': 'json',
            'address': address,
            'ak': 'Nq6xvK1GGytlV5jsztOnIxK3RhC7823N'}
    r = requests.get(url, params=Data)
    r.encoding = r.apparent_encoding
    if r.json()['status']==0:
        #r.json()['results'][0]['address_components']  
        #9 编号-街道-行政社区-区域-县-州-国家-邮编-邮政编码后缀
        #r.json()['results'][0]['formatted_address']详细地址
        lat = r.json()['result']['location']['lat']
        lng = r.json()['result']['location']['lng']
    else:
        print('status error')
    return lat,lng

if __name__ == '__main__': 
    address='河南省鹿邑县高集乡王屯行政村'
    lat,lng = Geocoding(address)
    print(address)
    print('lat:',lat,'\nlng:',lng)