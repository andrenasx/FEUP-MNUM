# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 21:12:06 2019

@author: fmna
"""

import math as m

def f1(x,y):
    return 2*x**2-x*y-5*x+1
    #return x*x-y-1.2

def f2(x,y):
    return x+3*m.log(x)-y**2
    #return -x+y*y-0.5
    
def gx(x,y):						#achando a funcao de x, com f1
	return m.pow((x*(y+5)-1)/2, 1/2)
    

def gy(x,y):						#achando a funcao y, com f2
	#return m.pow(x+m.log(x),1/2)
    return -m.pow(x+m.log(x),1/2)

def pp2Var(x,y,max_iter):
    for i in range(max_iter):
        xn=gx(x,y)
        yn=gy(x,y)
        print(i,xn,yn)
        x=xn
        y=yn