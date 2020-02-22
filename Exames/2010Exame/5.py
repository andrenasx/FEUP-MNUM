# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 10:58:08 2020

@author: fmna
"""

def f(x,y):
    return 6*x**2-x*y+12*y+y**2-8*x

def dfx(x,y):
    return -y+12*x-8

def dfy(x,y):
    return 2*y-x+12

def gradiente(x,y,h):
    for i in range(2):
        print(i)
        print("x: ",x)
        print("y: ",y)
        print("Z(x,y): ",f(x,y))
        print("df/dx: ",dfx(x,y))
        print("df/dy: ",dfy(x,y))
        print("")
        if(i==0):
            xn = x - h*dfx(x,y)
            yn = y - h*dfy(x,y)
            if (f(xn,yn) < f(x,y)):
                h *= 2
                y = yn
                x = xn
            elif (f(xn,yn) > f(x,y)):
                h/= 2
                
gradiente(0,0,0.25)