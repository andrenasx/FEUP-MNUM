# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 15:43:40 2019

@author: fmna
"""

def f(x,y):
    return y*y-2*x*y-6*y+2*x*x+12
def dfx(x,y):
    return 4*x - 2*y
def dfy(x,y):
    return 2*y-2*x-6

def gradient(x,y,h):
    for i in range(60): 
        xn = x - h*fx(x,y)
        yn = y - h*fy(x,y)
        if (f(xn,yn) < f(x,y)):
            h *= 2
            y = yn
            x = xn

        if (f(xn,yn) > f(x,y)):
            h/= 2
        print("%.10f, %.10f" %(xn, yn))
    return [x,y]

print(gradient(1,1,1))
k = gradient(1,1,1)
print(f(k[0],k[1]))