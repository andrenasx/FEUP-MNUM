# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 14:57:33 2020

@author: fmna
"""

def dz(y,z):
    return -7*z-4*y

def euler_2(x,y,z,h):
    for i in range(3):
        deltaz=dz(y,z)
        x+=h
        y+=h*z
        z+=h*deltaz
        print("x: ",x)
        print("y: ",y)
        print("y': ",z,"\n")
        
euler_2(0.4,2,1,0.2)