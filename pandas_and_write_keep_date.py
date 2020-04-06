# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 01:38:58 2020

@author: yomer
"""
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, shee_tname='Sheet1')

writer = pd.ExcelWriter(output_file)
data_frame.to_excel(writer, sheet_name='Sheet1_output', index=False)
writer.save()