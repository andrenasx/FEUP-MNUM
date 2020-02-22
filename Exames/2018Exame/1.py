# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 14:31:27 2020

@author: fmna
"""

import math as m

def f1(x,y):
    return m.sin(x+y)-m.exp(x-y)

def f2(x,y):
    return m.cos(x+y)-x**2*y**2

def df1x(x,y):
    return m.cos(y+x)-m.exp(x-y)

def df2x(x,y): 
    return -m.sin(y+x)-2*x*y**2

def df1y(x,y):
    return m.cos(y+x)+m.exp(x-y)

def df2y(x,y):
    return -m.sin(y+x)-2*y*x**2

def jacobian(x,y):
    return df1x(x,y)*df2y(x,y)-df1y(x,y)*df2x(x,y)

def hn(x,y):
    return -((f1(x,y)*df2y(x,y)-df1y(x,y)*f2(x,y))/jacobian(x,y))

def kn(x,y):
    return -((df1x(x,y)*f2(x,y)-f1(x,y)*df2x(x,y))/jacobian(x,y))

def newton_2(x,y):
    for i in range(2):
        xn=x+hn(x,y)
        yn=y+kn(x,y)
        print(i+1)
        print("x: ",x)
        print("y: ",y,"\n")
        x=xn
        y=yn
        
newton_2(0.5,0.25)