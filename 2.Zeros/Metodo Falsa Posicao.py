# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 19:16:56 2019

@author: fmna
"""

#Metodo Corda

def f(x):
    return 2*x**2 - 5*x - 2


def fp(a,b,p):
    x=(a*f(b)-b*f(a))/(f(b)-f(a))
    while abs(b-a) > p:
        if f(a)*f(x)<0:
            b=x
        else:
            a=x

        #\print (a,rr,b,f(rr))
    return (b+a)/2