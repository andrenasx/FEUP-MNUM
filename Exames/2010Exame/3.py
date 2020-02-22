# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 10:36:29 2020

@author: fmna
"""

from math import *

def dxt(x,t):
    return sin(x)+sin(2*t)

def rk4(x,t,tf,h):
    while(t<tf):
        d1=h*dxt(x,t)
        d2=h*dxt(x+d1/2,t+h/2)
        d3=h*dxt(x+d2/2,t+h/2)
        d4=h*dxt(x+d3,t+h)
        x+=(d1+d4)/6+(d2+d3)/3
        t+=h
        print("t: ",t)
        print("x: ",x)
    return x

rk4(0,1,1.5,0.125)

s=0.391238
s1=0.391503
s2=0.391517

QC=(s1-s)/(s2-s1)
print("QC: ",QC)