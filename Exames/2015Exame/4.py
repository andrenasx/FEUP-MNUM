# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 19:00:37 2020

@author: fmna
"""

from math import *

def g(x):
    return 2*log(2*x)

def pp(x):
    for i in range(1):
        x=g(x)
    return x

print( pp(1.1) )