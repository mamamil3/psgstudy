# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 23:20:46 2020

@author: yomer
"""

"""
def fv_f(pv,r,n):
    return pv*(1+r)**n
"""

def npv_f(rate, cashflows):
    total = 0.0
    for i in range(0,len(cashflows)):
        total += cashflows[i] / (1 + rate)**i
    return total

"""
def npv_fe(rate, cashflows):
    total = 0.0
    for i, cashflow in enumerate(cashflows):
        total += cashflow / (1 + rate)**i
    return total
"""

#npv를 0으로 만드는 할인율 계산식
cashFlows=(550,-500,-500,-500,1000)
r=0

while(r<1.0):
    r+=0.000001
    npv=npv_f(r,cashFlows)
    if(abs(npv)<=0.0001):
        print(r)
        