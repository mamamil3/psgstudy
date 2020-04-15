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
display = 100
start = 1
keyword = input("검색어 입력:")
result=[]
path = "C:/Users/yomer/Documents/파이썬스터디/"+keyword+"_keywordcount.csv"

def searchwb(display,start,keyword,page_count):
    url = "https://openapi.naver.com/v1/search/shop.xml"
    option = "&display="+str(display)+"&start="+str(start)    
    query = "?query="+urllib.parse.quote(keyword)
    url_query = url + query + option
    
    request = urllib.request.Request(url_query)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        
        
        xmlsoup = BeautifulSoup(response_body,'html.parser')
        items = xmlsoup.find_all('item')
    
        itemcount = start
        for item in items:
            if item.mallname.get_text() == shopname:
                print('<--------------------------')
                print('제목 : ' + item.title.get_text())
                print('샵명 : ' + item.mallname.get_text())
                print('순위 : ' + str(page_count+1) + 'page ' + str(itemcount-(display*page_count)))
                print('-------------------------->\n')
                
                #엑셀파일에 쓰기 위한 값 리스트 추가
                result.append([item.title.get_text()]+[item.mallname.get_text()]+[str(itemcount-(display*page_count))]+[page_count+1])
                #sys.exit()
            itemcount += 1
    else:
        print("Error Code:" + rescode)
    
#api 검색 최대치 1000건 이므로 1회한도 100건씩 10번 읽어오기!    
for i in range(0,25):
    
    print(start)
    #검색어로 상품찾기 함수 호출
    searchwb(display,start,keyword,i)
    
    if start < 500:
        start = start + display

#엑셀 파일에 기록하기
table = pd.DataFrame(result,columns=('title','mallname','ranking','page_count'))
table.to_csv(path,encoding="cp949",mode="w",index=True)    


