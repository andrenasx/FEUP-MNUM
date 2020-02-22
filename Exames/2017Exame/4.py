# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 15:59:06 2020

@author: fmna
"""

import os
import contextlib

from math import *

def dCt(T,C):
    return -exp(-0.5/(T+273))*C

def dTt(T,C):
    return 30*exp(-0.5/(T+273))*C-0.5*(T-20)

"""a"""
def euler(C,T,t,tf,h):
    i=0
    print("iteracao: ",i)
    print("t: ",t)
    print("C: ",C)
    print("T: ",T)
    while(t<tf):
        Cnext = C + h*dCt(T,C)
        Tnext = T + h*dTt(T,C)
        T=Tnext
        C=Cnext
        t+=h
        i+=1
        print("iteracao: ",i)
        print("t: ",t)
        print("C: ",C)
        print("T: ",T)
    return T
        
#euler(2.5,25,0,0.5,0.25)

"""b"""
def rk4(C,T,t,h):
    print("iteracao: 0")
    print("t: ",t)
    print("C: ",C)
    print("T: ",T)
    for i in range(2):
        d1 = h*dCt(T,C)
        D1 = h*dTt(T,C)
        d2 = h*dCt(T + (D1/2), C+ (d1/2))
        D2 = h*dTt(T + (D1/2), C+ (d1/2))
        d3 = h*dCt(T + (D2/2), C + (d2/2))
        D3 = h*dTt(T + (D2/2), C + (d2/2))
        d4 = h*dCt(T + D3, C + d3)
        D4 = h*dTt(T + D3, C + d3)
        Cnext = C + (d1/6) + (d2/3) + (d3/3) + (d4/6)
        Tnext = T + (D1/6) + (D2/3) + (D3/3) + (D4/6)

        T=Tnext
        C=Cnext
        t+=h
        
        print("iteracao: ",i+1)
        print("t: ",t)
        print("C: ",C)
        print("T: ",T)
        
#rk4(2.5,25,0,0.25)

"""c"""
def eulerC(C,T,t,tf,h):
    with open(os.devnull, "w") as f, contextlib.redirect_stdout(f):
        s=euler(C,T,t,tf,h)
    h/=2
    with open(os.devnull, "w") as f, contextlib.redirect_stdout(f):
        s1=euler(C,T,t,tf,h)
    print("h': ",h)
    print("T': ",s1)
    h/=2
    with open(os.devnull, "w") as f, contextlib.redirect_stdout(f):
        s2=euler(C,T,t,tf,h)
    print("h'': ",h)
    print("T'': ",s2)
    
    Q=(s1-s)/(s2-s1)
    print("Q: ",Q)
    err=(s2-s1)
    print("Erro: ",err)
    
#eulerC(2.5,25,0,0.5,0.25)
