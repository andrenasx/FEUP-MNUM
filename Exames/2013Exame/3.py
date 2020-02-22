# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 14:40:43 2020

@author: fmna
"""

def f(x,y):
    return 3*x**2-x*y+11*y+y**2-8*x

def dfx(x,y):
    return -y+6*x-8

def dfy(x,y):
    return 2*y-x+11

def gradient(x,y,h):
    for i in range(2):
        print(i)
        print("x: ",x)
        print("y: ",y)
        print("Z(x,y): ",f(x,y))
        print("dZ/dx: ",dfx(x,y))
        print("dZ/dy: ",dfy(x,y))
        print("")
   
        xn = x - h*dfx(x,y)
        yn = y - h*dfy(x,y)
        if (f(xn,yn) < f(x,y)):
            h *= 2
            y = yn
            x = xn

        elif (f(xn,yn) > f(x,y)):
            h/= 2

gradient(2,2,0.5)