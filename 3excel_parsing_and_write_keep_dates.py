# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 02:55:11 2020

@author: yomer
"""
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('Sheet1_output')

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('Sheet1')
    for row_index in range(worksheet.nrows):
        row_list_output = []
        for column_index in range(worksheet.ncols):
            if worksheet.cell_type(row_index, column_index) == 3:
                date_cell = xldate_as_tuple(worksheet.cell_value(row_index,column_index), workbook.datemode)
                date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                row_list_output.append(date_cell)
                output_worksheet.write(row_index, column_index, date_cell)
            else:
                non_date_cell = worksheet.cell_value(row_index, column_index)
                row_list_output.append(non_date_cell)
                output_worksheet.write(row_index, column_index, non_date_cell)
output_workbook.save(output_file)
