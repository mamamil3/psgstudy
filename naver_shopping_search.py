# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 02:08:29 2020

@author: yomer
"""
# 네이버 검색 Open API 예제 
import os
import sys
import urllib.request

txtpath = sys.argv[1]

# 텍스트파일에서 키 아이디, 시크릿 읽어오기
keyfile = open(txtpath,'r')
lines = keyfile.readlines()
keyfile.close()

# 개행문자 제거
idsecret = list(map(lambda s: s.strip(), lines))

client_id = idsecret[0]
client_secret = idsecret[1]


encText = urllib.parse.quote("두꺼운물티슈")
#url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
url = "https://openapi.naver.com/v1/search/shop.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    #print(response_body.decode('utf-8'))
    xmlfile = open("searchresult.xml",'w')
    xmlfile.write(response_body.decode('utf-8'))
    xmlfile.close()
else:
    print("Error Code:" + rescode)

