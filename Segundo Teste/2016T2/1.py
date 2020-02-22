    # -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 10:47:09 2019

@author: fmna
"""

import math as m

def dC(T,C):
    return -m.exp(-0.5/(T+273))*C

def dT(T,C):
    return  20*m.exp(-0.5/(T+273))*C-0.5*(T-20)

#a
def euler(t,tf,T,C,h):
    while(t<tf):
        Cn=C+h*dC(T,C)
        Tn=T+h*dT(T,C)
        t+=h
        C=Cn
        T=Tn
        print("C: ",C)
        print("T: ",T)
        print("")
    return C
euler(0,0.5,15,1,0.25)


#b
def rk4(t,tf,T,C,h):
    while(t<tf):
        t+=h
        
        d1=h*dC(T,C)
        d2=h*dC(T+h/2,C+d1/2)
        d3=h*dC(T+h/2,C+d2/2)
        d4=h*dC(T+h,C+d3)
        Cn=C+(d1/6+d2/3+d3/3+d4/6)
        
        d1=h*dT(T,C)
        d2=h*dT(T+d1/2,C+h/2)
        d3=h*dT(T+d2/2,C+h/2)
        d4=h*dT(T+d3,C+h)
        Tn=T+(d1/6+d2/3+d3/3+d4/6)
        
        C=Cn
        T=Tn
        print("C: ",C)
        print("T: ",T)
        print("")
    return 0
#rk4(0,0.5,15,1,0.25)


#c
def eulerQE(t,tf,T,C,h):
    C1=euler(t,tf,T,C,h)
    h/=2
    print("h': ",h)
    C2=euler(t,tf,T,C,h)
    h/=2
    print("h'': ",h)
    C3=euler(t,tf,T,C,h)
    print("C1: ",C1)
    print("C2: ",C2)
    Q=(C2-C1)/(C3-C2)
    print("Q: ",Q)
    err=(C3-C2)
    print("Erro: ",err)
    
    return 0
eulerQE(0,0.5,15,1,0.25)
