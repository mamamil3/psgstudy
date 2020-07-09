# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 23:20:46 2020

@author: yomer
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