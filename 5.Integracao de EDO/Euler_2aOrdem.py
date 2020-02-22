# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 15:30:11 2019

@author: fmna
"""

#z = dy/dx
#dz = d2y/dx2

def dz(x,z):
    return 2 + x**2 +x*z

h=0.25
x=1
y=1
z=0

def euler_2(x,y,z,h):
    for i in range(3):
        print("iteracao: ",i)
        deltaz=dz(x,z)
        x+=h
        y+=h*z
        z+=h*deltaz