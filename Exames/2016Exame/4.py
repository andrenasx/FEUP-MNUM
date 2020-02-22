# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 18:32:00 2020

@author: fmna
"""

def f(x):
    return x**7+0.5*x-0.5

def corda(a,b):
    for i in range(3):
        w=(a*f(b)-b*f(a))/(f(b)-f(a))
        print("xe: ",a)
        print("xd: ",b)
        print("xn: ",w)
        if f(a)*f(w)<0:
            b=w
        else:
            a=w

corda(0.656044,0.8)