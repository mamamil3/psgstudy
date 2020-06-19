# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 01:48:03 2020

@author: yomer
"""
#import sys
import pandas as pd
import datetime


# 오늘 날짜
dt = datetime.datetime.now()

#파일명 입력받기
input_file = input() 
output_file = 'ssInvoiceList_' + dt.strftime("%Y%m%d") + '.xls'
print('input_file: ' + input_file)

# 첫번째 시트 선택, 첫행 해더 선택 디폴트값
input_data_frame = pd.read_excel(input_file, sheet_name=0, header=0, dtype={'솔루션 주문번호':str }, index_col=None)

data_frame_column_by_name = input_data_frame.loc[:, ['솔루션 주문번호', '수취인명', '배송구분', '택배사', '송장번호']]
data_frame_column_by_name.columns = ['상품주문번호', '수취인', '배송방법', '택배사', '송장번호']
data_frame_column_by_name['배송방법'] = '택배,등기,소포'

writer = pd.ExcelWriter(output_file)
data_frame_column_by_name.to_excel(writer, sheet_name='Sheet1', index=False)
writer.save()

