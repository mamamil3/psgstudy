# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 02:08:29 2020

@author: yomer
"""
# 네이버 검색 Open API 예제 
#import os
import pandas as pd
import sys
import urllib.request
from bs4 import BeautifulSoup

txtpath = sys.argv[1]
shopname = sys.argv[2]

#엑셀 파일에 기록하기
def makeexel(items,path):
    result=[]
    for item in items:
        result.append([item.title.get_text()]+[item.mallname.get_text()])
    table = pd.DataFrame(result,columns=('title','mallname'))
    table.to_csv(path,encoding="cp949",mode="w",index=True)
    
# 텍스트파일에서 키 아이디, 시크릿 읽어오기
keyfile = open(txtpath,'r')
lines = keyfile.readlines()
keyfile.close()

# 개행문자 제거
idsecret = list(map(lambda s: s.strip(), lines))

client_id = idsecret[0]
client_secret = idsecret[1]


#url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
#url = "https://openapi.naver.com/v1/search/shop.xml?query=" + encText # xml 결과
url = "https://openapi.naver.com/v1/search/shop.xml"
option = "&display=40"    
query = "?query="+urllib.parse.quote(input("검색어 입력:"))
url_query = url + query + option

request = urllib.request.Request(url_query)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    #print(response_body.decode('utf-8'))
    
    xmlsoup = BeautifulSoup(response_body,'html.parser')
    items = xmlsoup.find_all('item')

    itemcount = 1
    for item in items:
        if item.mallname.get_text() == shopname:
            print('<--------------------------')
            print('제목 : ' + item.title.get_text())
            print('샵명 : ' + item.mallname.get_text())
            print('순위 : ' + str(itemcount))
            print('-------------------------->\n')
            #sys.exit()
        itemcount += 1
    makeexel(items, "C:/Users/yomer/Documents/파이썬스터디/navershoping_keywordcount.csv")
else:
    print("Error Code:" + rescode)

