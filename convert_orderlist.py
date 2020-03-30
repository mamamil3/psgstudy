# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 01:48:03 2020

@author: yomer
"""
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

input_data_frame = pd.read_excel(input_file, '발주발송관리', index_col=None)
data_frame_column_by_name = input_data_frame.loc[:, ['판매자 상품코드','수량','구매자명',
                                                     '구매자연락처', '수취인명', '수취인연락처1', 
                                                     '수취인연락처2', '우편번호', '배송지', '배송메세지',
                                                     '판매채널', '상품주문번호', '옵션정보']]
data_frame_column_by_name.columns = ['품목코드(*)', '수량(*)', '주문자이름(*)', 
                                     '주문자연락처(*)', '수령인이름(*)', '수령인연락처1(*)', 
                                     '수령인연락처2', '우편번호(*)', '주소지(*)', '배송요청사항', 
                                     '판매매체', '셀러주문No', '비고']

writer = pd.ExcelWriter(output_file)
data_frame_column_by_name.to_excel(writer, sheet_name='Sheet1', index=False)
writer.save()

