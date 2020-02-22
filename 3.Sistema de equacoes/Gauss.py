# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 18:21:14 2019

@author: fmna
"""

import copy as c

m=[[7,8,9,24],[8,9,10,27],[9,10,8,27]]
r=[0,0,0]
mc=c.deepcopy(m)
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

#Estabilidade Interna
def residuos(m):
    for eq in range(dimV):
        for sol in range(dimV):
            r[eq] = r[eq] + mc[eq][sol]*m[sol][dimV]
        r[eq] = mc[eq][dimV] - r[eq]
        
    return r

#Estabilidade Externa
"""
A*dx=db-dA*x

db-daA*x =    
[0.5,0.5,0.5]-[[0.5,0.5,0.5],[0.5,0.5,0.5],[0.5,0.5,0.5]]*[-4.3716,-8.9325,28.8401]
= [- 7.268,- 7.268,- 7.268]
"""

print("")
m=[[7,8,9,- 7.268],[8,9,10,- 7.268],[9,10,8,- 7.268]]
gauss(m)
print(m)