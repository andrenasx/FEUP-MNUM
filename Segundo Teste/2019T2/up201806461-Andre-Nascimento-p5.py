#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 18:34:45 2019

@author: exame
"""

#z=dy/dt
#dz/dt=d2y/dt2
def dz(t,z):
    return 1.5+t**2+t*z

def euler_2(t,y,z,h):
    #valores iniciais
    print("iteração: 0")
    print("t: ",t)
    print("y: ",y)
    print("--------")
    for i in range(2):
        deltaz=dz(t,z)
        t+=h
        y+=h*z
        z+=h*deltaz
        print("iteração: ",i+1)
        print("t: ",t)
        print("y: ",y)
        print("--------")

def rk4_2(t,y,z,h):
    #valores iniciais
    print("iteração: 0")
    print("t: ",t)
    print("y: ",y)  
    print("--------")
    for i in range(2):
        z1 = h*z
        deltaz1=h*dz(t,z)
        z2=h * (z + deltaz1/2)
        deltaz2=(h * (dz(t + h/2, z + deltaz1/2)))
        z3=h * (z + deltaz2/2)
        deltaz3=(h * (dz(t + h/2, z + deltaz2/2)))
        z4=h * (z + deltaz3)
        deltaz4=(h * (dz(t + h, z + deltaz3)))
        y+=z1/6 + z2/3 + z3/3 + z4/6
        z+=deltaz1/6 + deltaz2/3 + deltaz3/3 + deltaz4/6
        t+=h;
        print("iteracao: ",i)
        print("t: ",t)
        print("y: ",y)
        print("--------")
     
print("Euler:")
euler_2(1,0,1,0.2)
print("")
print("--------")
print("RK4:")
rk4_2(1,0,1,0.2)