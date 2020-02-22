# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:10:56 2019

@author: fmna
"""

#TRISSECCAO
#FUNCAO TEM DE SER CONVEXA ENTRE a E b

#METODO SECCAO AUREA
#B = (m.sqrt(5)-1)/2
#A = B**2

import math as m

def f(x):
    return m.sin(x)**2

def aurea(a,b,precisao):
    razao = ((m.sqrt(5)-1)/2)**2
    c = a + razao *(b-a)
    d = b - razao *(b-a)
    fc = f(c)
    fd = f(d)
    while (abs(b-a) > precisao):
        if (fc < fd):   #Metodo para minimos, maximo: trocar fc>df
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
            
    return [a,b]

#aurea(m.pi/2, 3/2*m.pi, 0.00001)