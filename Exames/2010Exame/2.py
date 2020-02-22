# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 10:32:40 2020

@author: fmna
"""

from math import *

def g(x):
    return 2*log(2*x)

def pp(x,numItr):
    print("0")
    print("x: ",x)
    for i in range(numItr):
        x=g(x)
        print("------")
        print(i+1)
        print("x: ",x)
        
pp(0.9,1)