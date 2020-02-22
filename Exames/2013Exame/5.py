# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 15:08:52 2020

@author: fmna
"""

from math import *

def f(x):
    return x-3.7+(cos(x+1.2))**3

def df(x):
    return 1-3*sin(x + 1.2)*(cos (x + 1.2))**2

def newton(x):
    x-=f(x)/df(x)
    return x

print(newton(3.8))