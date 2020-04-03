# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 02:55:11 2020

@author: yomer
"""
import sys
from xlrd import open_workbook
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('Sheet1_output')

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('Sheet1')
    for row_index in range(worksheet.nrows):
        for column_index in range(worksheet.ncols):
            output_worksheet.write(row_index, column_index, worksheet.cell_value(row_index, column_index))
output_workbook.save(output_file)
