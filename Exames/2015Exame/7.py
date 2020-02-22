# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 21:17:01 2020

@author: fmna
"""

from math import *

def f(x):
    return x**3-10*sin(x)+2.8

def bissec(a,b):
    for i in range(2):
        m=(a+b)/2
        if f(a)*f(m)<0:
            b=m
        else:
            a=m
    print(b)
    return b

bissec(1.5,4.2)