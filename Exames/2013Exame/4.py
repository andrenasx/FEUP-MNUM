# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 14:57:55 2020

@author: fmna
"""

from math import *

def f(x):
    return exp(1.5*x)

def simpson(a,b,h):
    total=f(a)+f(b)
    n=round((b-a)/h)
    for i in range(1,n,2):
        total+=4*(f(a+i*h))
    for i in range(2,n,2):
        total+=2*(f(a+i*h))
    total*=h/3
    return total

a=1
b=1.5
h=0.125
S=simpson(a,b,h)
print("h: ",h)
print("S: ",S)
h=h/2
S1=simpson(a,b,h)
print("h': ",h)
print("S': ",S1)
h=h/2
S2=simpson(a,b,h)
print("h'': ",h)
print("S'': ",S2)

QC=(S1-S)/(S2-S1)
print("QC = ",QC)
e=abs((S2-S1)/15)
print("err.rel. = ",e)
