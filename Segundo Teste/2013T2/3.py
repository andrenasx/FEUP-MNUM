# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 11:56:56 2019

@author: fmna
"""

import math as m

def f(x):
    return m.sqrt(1+(1.5*m.exp(1.5*x))**2)

def trap(a,b,h):
    n = round((b-a)/h)
    total=f(a)+f(b)
    for i in range(1,n):
        total+= 2*f(a+i*h)
    total*=h/2
    return total

def simp(a,b,h):
    n = round((b-a)/h)
    total=f(a)+f(b)
    for i in range(1,n,2):
        total+= 4*f(a+i*h)
    for i in range(2,n,2):
        total+= 2*f(a+i*h)
    total*=h/3
    return total

print("Trapezio")

L1=trap(0,1,0.25)
L2=trap(0,1,0.125)
L3=trap(0,1,0.0625)
print("L1 :",L1)
print("L2 :",L2)
print("L3 :",L3)

Q=(L2-L1)/(L3-L2)
print("QC: ",Q)

err=(L3-L2)/3
print("Err: ",err)

print("--------------")
print("Simpson")

L1=simp(0,1,0.25)
L2=simp(0,1,0.125)
L3=simp(0,1,0.0625)
print("L1 :",L1)
print("L2 :",L2)
print("L3 :",L3)

Q=(L2-L1)/(L3-L2)
print("QC: ",Q)

err=(L3-L2)/15
print("Err: ",err)