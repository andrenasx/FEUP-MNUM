# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 14:28:58 2019

@author: fmna
"""
#cx etc sao coeficientes das variaveis na matriz A
#s  o valor de b

def fx(cx,x,cy,y,cz,z,cw,w,s):
    return (s-cy*y-cz*z-cw*w)/cx

def fy(cx,x,cy,y,cz,z,cw,w,s):
    return (s-cx*x-cz*z-cw*w)/cy

def fz(cx,x,cy,y,cz,z,cw,w,s):
    return (s-cx*x-cy*y-cw*w)/cz

def fw(cx,x,cy,y,cz,z,cw,w,s):
    return (s-cx*x-cy*y-cz*z)/cw

def gaussSeidel(numItr):
    #guesses iniciais
    x=2.12687
    y=2.39858
    z=3.99517
    w=-3.73040
    for i in range(numItr):
        x = fx(6,x,0.5,y,3,z,0.25,w,25)
        y = fy(1.2,x,3,y,0.25,z,0.2,w,10)
        z = fz(-1,x,0.25,y,4,z,2,w,7,)
        w = fw(2,x,4,y,1,z,8,w,-12)
        
        print("x: ",x)
        print("y: ",y)
        print("z: ",z)
        print("w: ",w)
        print("")