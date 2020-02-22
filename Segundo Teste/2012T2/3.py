# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 17:36:59 2019

@author: fmna
"""

m=[[0.7,8,3,12],[-6,0.45,-0.25,15],[8,-3.1,1.05,23]]
dimV=len(m)

#Metodo de Gauss
def gauss(m):
    for diag in range(dimV):
        pivot = m[diag][diag]
        for col in range (dimV+1):
            m[diag][col]/=pivot
        for lin in range(diag+1, dimV):
            pivot2 = m[lin][diag]
            for col in range(diag, dimV+1):
                m[lin][col] -= m[diag][col] * pivot2
                
    #print(m)
    
    for diag in range(dimV-1, -1, -1):
        for lin in range(diag-1, -1, -1):
            factor=m[lin][diag]
            for col in range(dimV, diag-1, -1):
                m[lin][col]-=m[diag][col]*factor
    #print("")
    #print(m)
    return m

gauss(m)
print(m)

"""
A*dx=db-dA*x

db-daA*x =    
[0.5,0.5,0.5]-[[0.5,0.5,0.5],[0.5,0.5,0.5],[0.5,0.5,0.5]]*[-4.3716,-8.9325,28.8401]
= [- 7.268,- 7.268,- 7.268]
"""

print("")
m=[[0.7,8,3,- 7.268],[-6,0.45,-0.25,- 7.268],[8,-3.1,1.05,- 7.268]]
gauss(m)
print(m)