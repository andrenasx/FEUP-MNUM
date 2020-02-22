# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 15:35:38 2019

@author: fmna
"""

def f(x):
    if x==0:
        return 1.04
    elif x==0.25:
        return 0.37
    elif x==0.5:
        return 0.38
    elif x==0.75:
        return 1.49
    elif x==1:
        return 1.08
    elif x==1.25:
        return 0.13
    elif x==1.5:
        return 0.64
    elif x==1.75:
        return 0.84
    elif x==2:
        return 0.12

def simpson(a,b,h):
    total = f(a)
    n = round((b-a)/h)
    for i in range(1,n,2):
        #total+= 4*f[i]
        total+=4*f(a+i*h)
    for i in range(2,n,2):
        #total+= 2*f[i]
        total+=2*f(a+i*h)
    #total+= f[len(f)-1]
    total+= f(a+n*h)
    total*=h/3
    
    return total


#f = [1.04,1.08,0.12]
r1 = simpson(0,2,1)
#f = [1.04,0.38,1.08,0.64,0.12]
r2 = simpson(0,2,0.5)
#f = [1.04,0.37,0.38,1.49,1.08,0.13,0.64,0.84,0.12]
r3 = simpson(0,2,0.25)

print("valor: ",r3)

erro = (r3-r2)/15
print("erro: ", erro)