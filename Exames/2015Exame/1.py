# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 18:19:01 2020

@author: fmna
"""

def dTt(T):
    return -0.25*(T-37)

def euler(T,t,tf,h):
    while(t<tf):
        T+=h*dTt(T)
        t+=h
    print(T)
    return T

euler(3,5,5+2*0.4,0.4)