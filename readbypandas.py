# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 23:29:21 2020

@author: yomer
"""
import pandas as pd

url='httP://canisius.edu/~yany/data/ibm.csv'
x=pd.read_csv(url)
print(x[1:5])
