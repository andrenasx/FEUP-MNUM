# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 16:01:05 2019

@author: fmna
"""

#z = dy/dx
#dz = d2y/dx2

def dz(t,z):
    return 2 + t**2 +t*z

h=0.25
t=1
y=1
z=0

def euler(t,y,z,h):
    for i in range(3):
        print("iteracao: ",i)
        print("t : ",t)
        print("y: ",y)
        deltaz=dz(t,z)
        t+=h
        y+=h*z
        z+=h*deltaz
    
#euler(1,1,0,0.25)
        
def rk4(t,y,z,h):
    for i in range(3):
        print("iteracao: ",i)
        print("t : ",t)
        print("y: ",y)
        z1 = (h*z)
        dz1=h*dz(t,z)
        z2=(h * (z + dz1 / 2))
        dz2=(h * (dz(t + h/2, z + dz1 / 2)))
        z3=(h * (z + dz2 / 2))
        dz3=(h * (dz(t + h/2, z + dz2 / 2)))
        z4=(h * (z + dz3))
        dz4=(h * (dz(t + h, z + dz3)))
        y+=z1 / 6 + z2 / 3 + z3 / 3 + z4 / 6
        z+=dz1 / 6 + dz2 / 3 + dz3 / 3 + dz4 / 6
        t+=h;
        
#rk4(1,1,0,0.25)