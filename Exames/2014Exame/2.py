# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 10:55:12 2020

@author: fmna
"""

from math import *

def g(x):
    return -x+40*cos(sqrt(x))+3

def dg(x):
    return -1-20*sin(sqrt(x))/sqrt(x)

def newton(x):
    print("xn: ",x)
    print("g(xn): ",g(x))
    for i in range(2):
        x-=(g(x)/dg(x))
        print("xn: ",x)
        print("g(xn): ",g(x))
        
newton(1.7)