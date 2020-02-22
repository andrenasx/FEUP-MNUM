# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 17:17:37 2019

@author: fmna
"""

def fx(cx,x,cy,y,cz,z,cw,w,b):
    return (b-(cy*y+cz*z+cw*w))/cx

def fy(cx,x,cy,y,cz,z,cw,w,b):
    return (b-(cx*x+cz*z+cw*w))/cy

def fz(cx,x,cy,y,cz,z,cw,w,b):
    return (b-(cy*y+cx*x+cw*w))/cz

def fw(cx,x,cy,y,cz,z,cw,w,b):
    return (b-(cy*y+cz*z+cx*x))/cw

def gaussSeidel(numItr):
    x=0
    y=0
    z=0
    w=0
    for i in range(numItr):
        x=fx(4.8,x,-1,y,-1,z,1,w,1)
        y=fy(-1,x,4.8,y,1,z,-1,w,-1)
        z=fz(-1,x,2,y,4.8,z,-1,w,-1)
        w=fw(2,x,-1,y,-1,z,4.8,w,0)
        print("x: ",x)
        print("y: ",y)
        print("z: ",z)
        print("w: ",w)
        print("")
        
#gaussSeidel(2)