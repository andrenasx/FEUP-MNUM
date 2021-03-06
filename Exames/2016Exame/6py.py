# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 18:09:03 2020

@author: fmna
"""

from math import *

def f(x):
    return sqrt(1+(1.5*exp(1.5*x))**2)

"""Trapezios"""
print("Trapezios")

def trapezio(a,b,h):
    n = int(abs((b-a)/h))
    total = 0
    for i in range(1,n):
        total += 2*f(a+i*h)

    total+= f(a)+f(a+n*h)
    total *= h/2
    return total 

# Calculo do coeficiente de convergencia
r1 = trapezio(0,2,0.5)
r2 = trapezio(0,2,0.5/2)
r3 = trapezio(0,2,0.5/4)

coeficiente = (r2-r1)/(r3-r2) 
print("r1:",r1)
print("r2:",r2)
print("r3", r3)
print("coeficiente:", coeficiente)

# Calculo do erro 
erro = (r3-r2)/3
print("erro:", abs(erro))


"""Simpson"""
print("Simpson")

def simpson(a,b,h):
    total = 0
    n = int(abs((b-a)/h))
    for i in range(1,n,2):  #odd values
        total += 4*f(a+i*h)
    for i in range(2,n,2):  #even values 
        total+= 2*f(a+i*h)

    total+= f(a)+f(a+n*h)   #get the first value and last value
    total *= h/3

    return total 

# Calculo da convergencia
r1 = simpson(0,2,0.5)
r2 = simpson(0,2,0.5/2)
r3 = simpson(0,2,0.5/4)

coeficiente = (r2-r1)/(r3-r2)
 
print("r1:",r1)
print("r2:",r2)
print("r3", r3)
print("coeficiente:", coeficiente)

# Calculo do erro
erro = (r3-r2)/15
print("erro:", abs(erro)) # erros sempre em modulo