# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 01:44:08 2020

@author: yomer
"""
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)
# 'Sale Amount'열의 값이 1400.00보다 큰 모든 행을 원한다.
data_frame_value_meets_condition = data_frame[data_frame['Sale Amount'].astype(float) > 1400.0]

writer = pd.ExcelWriter(output_file)
data_frame_value_meets_condition.to_excel(writer, sheet_name= 'jan_13_output', index=False)