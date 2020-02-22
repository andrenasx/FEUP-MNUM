# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 19:21:53 2019

@author: fmna
"""

#arbitrado delta(x) = h

import math as m

def f(x,y):
    return m.sin(x)

def rk4(x,y,xf,h):
    while (x < xf):
        delta_1 = h*f(x,y)
        delta_2 = h*f(x + (h/2), y+ (delta_1/2))
        delta_3 = h*f(x + (h/2), y + (delta_2/2))
        delta_4 = h*f(x + h, y + delta_3)
        
        y = y + (delta_1/6) + (delta_2/3) + (delta_3/3) + (delta_4/6)
        
        x = x + h
    return y

r1 = rk4(0,0,6,2*m.pi/160)
r2 = rk4(0,0,6,2*m.pi/320)
r3 = rk4(0,0,6,2*m.pi/640)

print("s1 =", r1) 
print("s2 =", r2)
print("s3 =", r3)

quociente = (r2-r1)/(r3-r2)
print("quociente =", quociente)
erro = (r3-r2)/15
print("Erro =", erro)