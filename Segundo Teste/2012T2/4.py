# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 17:28:41 2019

@author: fmna
"""

def dvu(u,v):
    return u*(u/2+1)*v**3+(u+5/2)*v**2

def euler(u,uf,v,h):
    while(u<uf):
        v+=h*dvu(u,v)
        u+=h
    return v

S=euler(1,1.8,0.1,0.08)
S1=euler(1,1.8,0.1,0.04)
S2=euler(1,1.8,0.1,0.02)
QC=(S1-S)/(S2-S1)
err=S2-S1
print(S)
print(S1)
print(S2)
print(QC)
print(err)