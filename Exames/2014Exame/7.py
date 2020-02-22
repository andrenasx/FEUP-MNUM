# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 11:53:37 2020

@author: fmna
"""

def g(x):
    return (4*x**3-x+3)**(1/4)

def pp(x):
    for i in range(2):
        x=g(x)
        print(x)
        
pp(3.5)