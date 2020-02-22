#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 18:21:15 2019

@author: exame
"""

def dvu(u,v):
    return u*(u/2 + 1)*v**3 + (u + 5/2)*v**2

def rk4(u,uf,v,h):
    while (u < uf):
        d1 = h*dvu(u,v)
        d2 = h*dvu(u + (h/2), v+ (d1/2))
        d3 = h*dvu(u + (h/2), v + (d2/2))
        d4 = h*dvu(u + h, v + d3)
        v+= (d1/6) + (d2/3) + (d3/3) + (d4/6)
        u+= h
    return v

#h=0.08
S=rk4(1,1.8,0.15,0.08)
#h'=0.08/2=0.04
S1=rk4(1,1.8,0.15,0.04)
#h''=0.04/2=0.02
S2=rk4(1,1.8,0.15,0.02)
QC=(S1-S)/(S2-S1)
E=abs((S2-S1)/15)

print("Usando h, v(1,8)= ",S)
print("Usando h', v(1,8)= ",S1)
print("Usando h'', v(1,8)= ",S2)
print("QC= ",QC)
print("Erro= ",E)