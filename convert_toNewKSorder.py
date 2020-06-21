# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 01:48:03 2020

@author: yomer
"""
import sys
import pandas as pd
import os
import datetime

#path = "./"
#엑셀파일이 있는 폴더경로 지정
#path = sys.argv[1]
path = input()

file_list = os.listdir(path)
file_list_xlsx = [file for file in file_list if file.startswith('스마트스토어_선택주문조회_')]

if len(file_list_xlsx) < 1:
    print("파일이 존재하지 않습니다.")
    sys.exit(1)

dt = datetime.datetime.now()

input_file = path + '/' + file_list_xlsx[0]
output_file = path + '/excel_order_' + dt.strftime("%Y%m%d") + '.xls'
print('input_file: ' + input_file)

#엑셀파일에서 불러올 때 2번째 행부터 읽어오도록 지정 header=1
#특정 컬럼의 데이터타입 지정(엑셀 쓰기 할때 숫자앞에 0삭제되는거 방지, 큰숫자 표시 ) dtype=텍스트
input_data_frame = pd.read_excel(input_file, '발주발송관리', header=1, dtype={'우편번호':str, '상품주문번호':str }, index_col=None)


data_frame_column_by_name = input_data_frame.loc[:, ['판매자 상품코드','수량','옵션정보',
                                                     '옵션관리코드', '수취인명', '수취인연락처1', 
                                                     '수취인연락처2', '우편번호', '배송지', '배송메세지',
                                                     '판매채널', '상품주문번호', '옵션정보']]
data_frame_column_by_name.columns = ['상품번호(*)', '수량(*)', '선택옵션1', 
                                     '선택옵션2', '수취인명(*)', '수취인휴대폰(*)', 
                                     '수취인전화', '우편번호(*)', '수취 주소(*)', '배송요청사항', 
                                     '주문관리메모', '주문관리메모2', '옵션내용']

# 파이썬 파일과 같은 폴더내에 있는 ks일괄등록 양식 읽어오기 
input_file2 = 'C:\\Users\yomer\\Documents\\쇼핑몰\\케이셀러\\주문서일괄등록엑셀파일\\excel_order.xls'
excel_order_data_frame = pd.read_excel(input_file2, 'Sheet1', header=2, index_col=None)
# dataframe 값 합치기
#excel_order_data_frame.append(data_frame_column_by_name, ignore_index=True)


writer = pd.ExcelWriter(output_file)
excel_order_data_frame.to_excel(writer, sheet_name='Sheet1', index=False)
writer.save()
print('output_file: ' + output_file)

