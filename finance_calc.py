# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 22:22:27 2020

@author: yomer
"""
import scipy as sp

# 미래가치 구하기 : 연금리 10%, 100달러 예금 2년 후
print(sp.fv(0.1, 2, 0, 100))

# 현재가치 구하기 : 금리1.45%, 횟수5, 미래가치 234
print(sp.pv(0.0145, 5, 0, 234))

# 10억 연리5% 현재가치
print(sp.pv(0.05, 10, 0, 10))

