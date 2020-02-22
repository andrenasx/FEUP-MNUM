# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 17:42:30 2020

@author: fmna
"""

#z = dy/dx
#dz = d2y/dx2

def dz(x,z):
    return 0.5+x**2+x*z

h=0.25
x=0
y=0
z=1

def euler_2(x,y,z,h):
    for i in range(2):
        print("iteracao: ",i+1)
        deltaz=dz(x,z)
        x+=h
        y+=h*z
        z+=h*deltaz
        print("t: ",x)
        print("y: ",y)

#euler_2(x,y,z,h)

def rk4_2(x,y,z,h):
    for i in range(2):
        print("iteracao: ",i)
        z1 = (h*z)
        dz1=h*dz(x,z)
        z2=(h * (z + dz1/2))
        dz2=(h * (dz(x + h/2, z + dz1/2)))
        z3=(h * (z + dz2/2))
        dz3=(h * (dz(x + h/2, z + dz2/2)))
        z4=(h * (z + dz3))
        dz4=(h * (dz(x + h, z + dz3)))
        y+=z1/6 + z2/3 + z3/3 + z4/6
        z+=dz1/6 + dz2/3 + dz3/3 + dz4/6
        x+=h;
        print("t: ",x)
        print("y: ",y)
        
rk4_2(x,y,z,h)