# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 23:29:21 2020

@author: yomer
"""
# import pandas as pd

# #url='httP://canisius.edu/~yany/data/ibm.csv'
# path = 'test.csv'
# x=pd.read_csv(path)
# print(x[1:5])
import pandas_datareader.data as web
import datetime

start = datetime.datetime(2020, 2, 19)
end = datetime.datetime(2020, 3, 4)

# df = web.DataReader("078930.KS", "yahoo", start, end)
df =web.get_data_yahoo("078930.KS")

print(df)