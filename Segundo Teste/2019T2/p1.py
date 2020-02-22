#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 18:10:09 2019

@author: exame
"""


def W(t):
    if t==0:
        return 0.0
    elif t==1:
        return 0.0210844012
    elif t==2:
        return 0.4003504188
    elif t==3:
        return 2.0588364952
    elif t==4:
        return 6.5316067009
    elif t==5:
        return 15.9677507346
    elif t==6:
        return 33.1303839233
    elif t==7:
        return 61.3966472222
    elif t==8:
        return 104.7577072145
    elif t==9:
        return 167.8187561119
    elif t==10:
        return 255.7990117542
    elif t==11:
        return 374.5317176093
    elif t==12:
        return 530.4641427735
    elif t==13:
        return 730.6575819712
    elif t==14:
        return 982.7873555549
    elif t==15:
        return 1295.1428095056
    elif t==16:
        return 1676.6273154323
    
def simpson(t0,t1,h):
    n = round((t1-t0)/h)
    total=W(t0)+W(t0+n*h)
    for i in range(1,n,2):
        total+=4*W(t0+i*h)
    for i in range(2,n,2):
        total+=2*W(t0+i*h)
    total/=3
    return total

print("Wtotal= ",simpson(0,16,1))
    
s=simpson(0,16,4)
s1=simpson(0,16,2)
s2=simpson(0,16,1)
QC=(s1-s)/(s2-s1)
E=(s2-s1)/15
print("QC: ",QC)
print("Erro: ",E)
