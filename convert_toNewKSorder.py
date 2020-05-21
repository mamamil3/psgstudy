# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 01:48:03 2020

@author: yomer
"""
import sys
import pandas as pd
import os
import datetime

path = "./"
file_list = os.listdir(path)
file_list_xlsx = [file for file in file_list if file.startswith('스마트스토어_선택주문조회_')]

if len(file_list_xlsx) < 1:
    print("파일이 존재하지 않습니다.")
    sys.exit(1)

dt = datetime.datetime.now()

input_file = file_list_xlsx[0]
output_file = 'excel_order_' + dt.strftime("%Y%m%d") + '.xls'
print(input_file)

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

writer = pd.ExcelWriter(output_file)
data_frame_column_by_name.to_excel(writer, sheet_name='Sheet1', index=False)
writer.save()

