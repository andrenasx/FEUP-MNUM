# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 21:02:37 2019

@author: fmna
"""

def simpson(a,b,h):
    n = round((b-a)/h)
    total = f[0]+f[len(f)-1]
    for i in range(1,n,2):
        total += 4*f[i]
    for i in range(2,n,2):
        total += 2*f[i]
    total *= h/3
    return total

f=[0.18,0.88,0.43]
s=simpson(0,1.6,0.8)
f=[0.18,0.83,0.88,0.8,0.43]
s1=simpson(0,1.6,0.4)
f=[0.18,0.91,0.83,1.23,0.88,1.37,0.8,1.34,0.43]
s2=simpson(0,1.6,0.2)
err=(s2-s1)/15

print("valor: ",s2)
print("erro: ",err)