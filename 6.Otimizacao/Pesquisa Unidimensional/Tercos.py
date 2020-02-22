# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 14:58:05 2019

@author: fmna
"""

#PESQUISA UNIDIMENSIONAL
#TRISECÇÃO
#FUNCAO TEM DE SER CONVEXA ENTRE a E b

#METODO DOS TERÇOS : RAZAO = 1/3

import math as m

def f(x):
    return m.sin(x)**2

def tercos(a,b,precisao):
    razao = 1/3
    while (abs(b-a) > precisao):
        c = a + razao *(b-a)
        d = b - razao *(b-a)
        if (f(c) < f(d)):
            b = d
        else: 
            a = c
            
    return [a,b]

#tercos(m.pi/2, 3/2*m.pi, 0.00001)