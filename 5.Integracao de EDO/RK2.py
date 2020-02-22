# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 16:47:38 2019

@author: fmna
"""

#arbitrado delta(x) = h

import math as m

def f(x,y):
    return m.sin(x)

def rk2(x,y,xf,h):
    while (x < xf):
        y = y + h*f(x+h/2,y+h/2*f(x,y))
        x = x + h
    return y

r1 = rk2(0,0,6,2*m.pi/160)
r2 = rk2(0,0,6,2*m.pi/320)
r3 = rk2(0,0,6,2*m.pi/640)

print("s1 =", r1) 
print("s2 =", r2)
print("s3 =", r3)

quociente = (r2-r1)/(r3-r2)
print("quociente =", quociente)
erro = (r3-r2)/3
print("Erro =", erro)