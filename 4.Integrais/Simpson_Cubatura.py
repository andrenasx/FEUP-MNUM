# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 18:23:00 2019

@author: fmna
"""

total = 0
hx=1
hy=1
xy = [[1.1,1.4,7.7],[2.1,3.1,2.2],[7.3,1.5,1.2]]

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