# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 11:01:13 2019

@author: fmna
"""

import math as m

def f1(x,y):
    return 2*x**2-x*y-5*x+1
    #return x*x-y-1.2
    #return x*x+x*y-10

def f2(x,y):
    return x+3*m.log10(x)-y**2
    #return -x+y*y-0.5
    #return y+3*x*y*y-57

def df1x(x,y):
	return -y+4*x-5
    #return 2*x
    #return y+2*x

def df2x(x,y): 
    return 3/(m.log(10)*x)+1
    #return -1
    #return 3*y*y

def df1y(x,y):
	return -x
    #return -1
    #return x

def df2y(x,y):
	return -2*y
    #return 2*y
    #return 6*x*y+1

def jacobian(x,y):
    return df1x(x,y)*df2y(x,y)-df1y(x,y)*df2x(x,y)

def hn(x,y):
    return -((f1(x,y)*df2y(x,y)-df1y(x,y)*f2(x,y))/jacobian(x,y))

def kn(x,y):
    return -((df1x(x,y)*f2(x,y)-f1(x,y)*df2x(x,y))/jacobian(x,y))

def newton2var(x,y,max_iter): 
    for i in range(max_iter):
        xn=x+hn(x,y)
        yn=y+kn(x,y)
        print(i,xn,yn)
        x=xn
        y=yn

def newton2varErr(x,y,p):
    i=0
    xn=x+hn(x,y)
    yn=y+kn(x,y)
    print (i,xn,yn)
    while(abs(xn-x)>p or abs(yn-y)>p):
        i+=1
        x=xn
        y=yn
        xn=x+hn(x,y)
        yn=y+kn(x,y)
        print(i,xn,yn)
        
    