# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 14:49:48 2020

@author: fmna
"""

total = 0
hx=1
hy=1
xy = [[1.1,1.4,9.8],[2.1,4,2.2],[7.8,1.5,1.2]]

for i in range(len(xy)):
    for j in range(len(xy)):
        if((i==0 or i==len(xy)-1) and (j==0 or j==len(xy)-1)):
            total+=xy[i][j]
        elif(i==0 or i==len(xy)-1 or j==0 or j==len(xy)-1):
            total+=4*xy[i][j]
        else:
            total+=16*xy[i][j]
            
total*=(hx*hy)/9
print("valor: ",total)