# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 18:17:09 2019

@author: fmna
"""

import math as m

def f(x): 
    #return x**2; #[0,2]
    return m.sin(x) #[pi/2,pi]

def trapezio(a,b,n):
    h = abs((b-a)/n)
    total = 0
    for i in range(1,n):
        total += 2*f(a+i*h)

    total+= f(a)+f(a+n*h)
    total *= h/2
    return total 

# Calculo do coeficiente de convergencia

r1 = trapezio(m.pi/2,m.pi,100)
r2 = trapezio(m.pi/2,m.pi,200)
r3 = trapezio(m.pi/2,m.pi,400)

coeficiente = (r2-r1)/(r3-r2) 
print("r1:",r1)
print("r2:",r2)
print("r3", r3)
print("coeficiente:", coeficiente)

# Calculo do erro 

erro = (r3-r2)/3
print("erro:", abs(erro))
