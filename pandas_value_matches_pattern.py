# -*- coding: utf-8 -*-
"""
Created on Mon May 25 23:23:01 2020

@author: yomer
"""
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)


