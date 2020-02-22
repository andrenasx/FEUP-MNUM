# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 17:30:08 2020

@author: fmna
"""

def f1(x,y):
    return x**2-y-1.2

def f2(x,y):
    return -x+y**2-1
    
def df1x(x,y):
    return 2*x

def df2x(x,y): 
    return -1

def df1y(x,y):
    return -1

def df2y(x,y):
    return 2*y

def jacobian(x,y):
    return df1x(x,y)*df2y(x,y)-df1y(x,y)*df2x(x,y)

def hn(x,y):
    return -((f1(x,y)*df2y(x,y)-df1y(x,y)*f2(x,y))/jacobian(x,y))

def kn(x,y):
    return -((df1x(x,y)*f2(x,y)-f1(x,y)*df2x(x,y))/jacobian(x,y))

def newton2var(x,y,max_iter):
    for i in range(max_iter):
        xn=x+hn(x,y)
        yn=y+kn(x,y)
        print(i,xn,yn)
        x=xn
        y=yn
        
newton2var(1,1,2)