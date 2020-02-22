# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 21:16:39 2019

@author: fmna
"""

def dyx(x,y):
    return -0.25*(y-42)

def euler(T,t,tf,h):
    while(t<tf):
        T+=h*dyx(t,T)
        t+=h
    return T

#euler(10,5,5+2*0.4,0.4)