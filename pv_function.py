# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 23:20:49 2020

@author: yomer
"""
def pv_f(fv,r,n):
    """objective: 현재가치를 계산
    
    fv : 미래가치
    r : 기간별 할인율
    n : 총 기간 수
    
    
    """
    return fv/(1+r)**n

