# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 11:28:34 2020

@author: fmna
"""

from math import *

def f(x):
    return 5*cos(x)-sin(x)

def aurea(a,b,c,d):
    razao = ((sqrt(5)-1)/2)**2
    fc = f(c)
    fd = f(d)
    for i in range(2):
        if (fc < fd):
            b = d
            d = c
            fd = fc
            c = a + razao *(b-a)
            fc = f(c)
        else: 
            a = c
            c = d
            fc = fd
            d = b - razao *(b-a)
            fd = f(d)
        print("x1: ",a)
        print("x2: ",b)
        print("x3: ",c)
        print("x4: ",d)
        print("f(x1): ",f(a))
        print("f(x2): ",f(b))
        print("f(x3): ",f(c))
        print("f(x4): ",f(d))
        print("---")
        
aurea(2,4,2.76393,3.23606)