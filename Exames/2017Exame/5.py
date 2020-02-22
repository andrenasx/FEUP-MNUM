# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 16:58:32 2020

@author: fmna
"""

def f(x,y):
    return -1.1*x*y+12*y+7*x**2-8*x
def dfx(x,y):
    return -1.1*y+14*x-8
def dfy(x,y):
    return 12-1.1*x

def gradient(x,y,h):
    for i in range(1): 
        xn = x - h*dfx(x,y)
        yn = y - h*dfy(x,y)
        if (f(xn,yn) < f(x,y)):
            h *= 2
            y = yn
            x = xn

        elif (f(xn,yn) > f(x,y)):
            h/= 2
    return [x,y]

k = gradient(3,1,0.1)
print(f(k[0],k[1]))
