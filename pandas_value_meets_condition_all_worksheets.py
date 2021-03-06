# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 23:12:17 2020

@author: yomer
"""
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

# 모든 시트 읽기 sheet_name=None
data_frame = pd.read_excel(input_file, sheet_name = None, index_col=None)

row_output = []

for worksheet_name, data in data_frame.items():
    row_output.append(data[data['Sale Amount'].replace('$', '').replace(',', '').astype(float) > 2000.0])
filtered_rows = pd.concat(row_output, axis=0, ignore_index=True)

writer = pd.ExcelWriter(output_file)
filtered_rows.to_excel(writer, sheet_name='sale_amount_gt2000', index=False)
writer.save()

