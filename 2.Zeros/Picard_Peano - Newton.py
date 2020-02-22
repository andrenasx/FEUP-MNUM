# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 17:33:53 2019

@author: fmna
"""

#Expressao de f(x)
def f(x):
    return 2*x**2-5*x-3
    
#Expressao da derivada de f(x) 
def fl(x):
    return 4*x-5

#Expressao da funcao em ordem a x
def g(x):
    return 0.4*x**2-0.6


def picard_peano(x, max_iter, p):   
    for i in range(max_iter):
        xn=g(x)
        print(i,x)
        if abs(xn-x)<p:
            return (i, xn)
        x=xn

    
def newton(x, max_iter):
    for i in range(max_iter):
        x = x - (f(x)/fl(x))
        print(i, x)
        
#OU

def newton2(x):
    xn = x - (f(x)/fl(x))
    while x!=xn:
        x=xn
        xn = xn - (f(xn)/fl(xn))
        print(x,xn)