# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 17:00:29 2019

@author: fmna
"""

total = 0
xy = [[1.1,1.5,2.6],[2.1,4.9,2.2],[6.3,1.5,1.2]]

for i in range(len(xy)):
    for j in range(len(xy)):
        if((i==0 or i==len(xy)-1) and (j==0 or j==len(xy)-1)):
            total+=xy[i][j]
        elif(i==0 or i==len(xy)-1 or j==0 or j==len(xy)-1):
            total+=4*xy[i][j]
        else:
            total+=16*xy[i][j]
            
#total=xy[0][0]+xy[0][2]+xy[2][0]+xy[2][2]+4*(xy[1][0]+xy[0][1]+xy[2][1]+xy[1][2])+16*xy[1][1]
            
total*=(0.9*0.9)/9
print("valor: ",total)