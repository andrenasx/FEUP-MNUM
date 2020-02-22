# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 14:17:59 2020

@author: fmna
"""

#z=dy/dt
#dz/dt=d2y/dt2

def dz(t,z):
    return 0.5+t**2+t*z

def euler(t,y,z,h):
    for i in range(2):
        y+=h*z
        z+=h*dz(t,z)
        t+=h
        print(i+1)
        print("t: ",t)
        print("y: ",y)

def rk4(t,y,z,h):
    for i in range(2):
        z1 =h*z
        dz1=h*dz(t,z)
        z2=h * (z + dz1/2)
        dz2=h * (dz(t + h/2, z + dz1/2))
        z3=h * (z + dz2/2)
        dz3=h * (dz(t + h/2, z + dz2/2))
        z4=h * (z + dz3)
        dz4=h * (dz(t + h, z + dz3))
        y+=z1/6 + z2/3 + z3/3 + z4/6
        z+=dz1/6 + dz2/3 + dz3/3 + dz4/6
        t+=h;
        print(i+1)
        print("t: ",t)
        print("y: ",y)
        
print("Euler:")
euler(0,0,1,0.25)
print("")
print("RK4:")
rk4(0, 0, 1, 0.25)
