# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 21:25:59 2019

@author: fmna
""" 

def fx(cx,x,cy,y,cz,z,cw,w,b):
    return (b-(cy*y+cz*z+cw*w))/cx

def fy(cx,x,cy,y,cz,z,cw,w,b):
    return (b-(cx*x+cz*z+cw*w))/cy

def fz(cx,x,cy,y,cz,z,cw,w,b):
    return (b-(cx*x+cy*y+cw*w))/cz

def fw(cx,x,cy,y,cz,z,cw,w,b):
    return (b-(cx*x+cy*y+cz*z))/cw

def seidel(numItr):
    x=0
    y=0
    z=0
    w=0
    for i in range(numItr):
        x=fx(6,x,0.5,y,3,z,0.25,w,2.5)
        y=fy(1.2,x,3,y,0.25,z,0.2,w,3.8)
        z=fz(-1,x,0.25,y,4,z,2,w,10)
        w=fw(2,x,4,y,1,z,8,w,7)
    return [x,y,z,w]

#seidel(1)