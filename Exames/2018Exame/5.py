# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 14:57:33 2020

@author: fmna
"""

import math as m

def f(x):
    return (x-1)**2+x**4

def aurea(a,b,precisao):
    razao = ((m.sqrt(5)-1)/2)**2
    c = a + razao *(b-a)
    d = b - razao *(b-a)
    fc = f(c)
    fd = f(d)
    while (abs(b-a) > precisao):
        if (fc < fd):   #Metodo para minimos, maximo: trocar fc>fd
            b = d
            #fb = fd
            d = c
            fd = fc
            c = a + razao *(b-a)
            fc = f(c)
        else: 
            a = c
            #fa = fc
            c = d
            fc = fd
            d = b - razao *(b-a)
            fd = f(d)
            
    return [a,b,c,d]

print(aurea(0.5,0.8,0.00001))