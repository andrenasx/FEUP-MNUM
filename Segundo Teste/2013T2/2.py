# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 11:48:52 2019

@author: fmna
"""

import math as m

def f(x,y):
    return m.sin(2*x)+m.sin(2*y)

def rk4(t,tf,x,h):
    while(t<tf):
        d1=h*f(x,t)
        d2=h*f(x+d1/2,t+h/2)
        d3=h*f(x+d2/2,t+h/2)
        d4=h*f(x+d3,t+h)
        x+=d1/6 + d2/3 + d3/3 + d4/6
        t+=h
        print("t: ",t)
        print("x: ",x)
        print("---")
    return x
        
s=rk4(1,1.5,1,0.5)
s1=rk4(1,1.5,1,0.25)
s2=rk4(1,1.5,1,0.125)

QC=(s1-s)/(s2-s1)
print("QC: ",QC)