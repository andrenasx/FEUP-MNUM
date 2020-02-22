# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 19:02:52 2019

@author: fmna
"""

import math as m

def f(x): 
    #return x**2; #[0,2]
    return m.sin(x) #[pi/2,pi]
    
def simpson(a,b,n):
    total = 0
    h = (b-a)/n
    for i in range(1,n,2):  #odd values
        total += 4*f(a+i*h)
    for i in range(2,n,2):  #even values 
        total+= 2*f(a+i*h)

    total+= f(a)+f(a+n*h)   #get the first value and last value
    total *= h/3

    return total 

# Calculo da convergencia
r1 = simpson(m.pi/2, m.pi, 200)
r2 = simpson(m.pi/2, m.pi, 400)
r3 = simpson(m.pi/2, m.pi, 800)

coeficiente = (r2-r1)/(r3-r2)
 
print("r1:",r1)
print("r2:",r2)
print("r3", r3)
print("coeficiente:", coeficiente)

# Calculo do erro
erro = (r3-r2)/15
print("erro:", abs(erro)) # erros sempre em modulo