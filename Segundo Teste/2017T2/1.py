# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 18:25:09 2019

@author: fmna
"""

m=[[18,-1,1,10],[3,-5,4,2],[6,8,29,-1]]
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
                  
    for diag in range(dimV-1, -1, -1):
        for lin in range(diag-1, -1, -1):
            factor=m[lin][diag]
            for col in range(dimV, diag-1, -1):
                m[lin][col]-=m[diag][col]*factor
                
    return m

#Estabilidade Externa
"""
A*dx=db-dA*x

db-daA*x =
= [0.1,0.1,0.1]-[[0.1,0.1,0.1],[0.1,0.1,0.1],[0.1,0.1,0.1]]*[0.552949,-0.15347,-0.10655]=
= [0.07071,0.07071,0.07071]
"""

m=[[18,-1,1,0.07071],[3,-5,4,0.07071],[6,8,29,0.07071]]
gauss(m)
print(m)