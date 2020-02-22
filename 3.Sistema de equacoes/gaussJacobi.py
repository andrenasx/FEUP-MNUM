# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 14:57:03 2019

@author: fmna
"""

#cx etc sao coeficientes das variaveis na matriz A
#b  o valor de B

def fx(cx,x,cy,y,cz,z,cw,w,b):
    return (b-cy*y-cz*z-cw*w)/cx

def fy(cx,x,cy,y,cz,z,cw,w,b):
    return (b-cx*x-cz*z-cw*w)/cy

def fz(cx,x,cy,y,cz,z,cw,w,b):
    return (b-cx*x-cy*y-cw*w)/cz

def fw(cx,x,cy,y,cz,z,cw,w,b):
    return (b-cx*x-cy*y-cz*z)/cw

def gaussJacobi(numItr):
    #guesses iniciais
    x=2.12687
    y=2.39858
    z=3.99517
    w=-3.73040
    for i in range(numItr):
        xAnt = x
        yAnt = y
        zAnt = z
        wAnt = w
        x = fx(6,xAnt,0.5,yAnt,3,zAnt,0.25,wAnt,25)
        y = fy(1.2,xAnt,3,yAnt,0.25,zAnt,0.2,wAnt,10)
        z = fz(-1,xAnt,0.25,yAnt,4,zAnt,2,wAnt,7)
        w = fw(2,xAnt,4,yAnt,1,zAnt,8,wAnt,-12)
        
        print("x: ",x)
        print("y: ",y)
        print("z: ",z)
        print("w: ",w)
        print("")