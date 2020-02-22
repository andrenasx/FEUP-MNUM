# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 11:36:26 2019

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

def gaussJacobi(numItr):
    x=0.25
    y=0.25
    z=0.25
    w=0.25
    for i in range(numItr):
        xn=fx(4.5,x,-1,y,-1,z,1,w,1)
        yn=fy(-1,x,4.5,y,1,z,-1,w,-1)
        zn=fz(-1,x,2,y,4.5,z,-1,w,-1)
        wn=fw(2,x,-1,y,-1,z,4.5,w,0)
        x=xn
        y=yn
        z=zn
        w=wn
        print("x: ",x)
        print("y: ",y)
        print("z: ",z)
        print("w: ",w)
        print("")