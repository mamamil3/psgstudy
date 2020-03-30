# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 03:04:16 2020

@author: yomer
"""
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, '발주발송관리', index=None)

data_frame_column_by_name = data_frame.loc[:, ['판매자 상품코드','수량','구매자명']]
data_frame_column_by_name.columns = ['품목코드', '수량', '주문자이름']

writer = pd.ExcelWriter(output_file)
data_frame_column_by_name.to_excel(writer, sheet_name='Sheet1', index=False)
writer.save()

