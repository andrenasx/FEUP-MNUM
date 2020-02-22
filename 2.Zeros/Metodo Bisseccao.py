# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 18:17:57 2019

@author: fmna
"""

import math

def f(x):
    #return 2*x**2 - 5*x - 2
    return math.exp(0.7*x)-x**2-0.5

def bissec(a,b,p):
    while abs(b-a) > p:
    #for i in range(p):
        m=(b+a)/2
        #print(a,b,m,f(a),f(b),f(m))
        if f(a)*f(m)<0:
            b=m
        else:
            a=m
        print (a,m,b,f(m))
        
    return (b+a)/2