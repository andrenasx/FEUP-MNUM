# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 11:06:42 2020

@author: fmna
"""
import copy as c
m=[[0.1,0.5,3,0.25,0],[1.2,0.2,0.25,0.2,1],[-1,0.25,0.3,2,2],[2,0.00001,1,0.4,3]]
r=[0,0,0]
mc=c.deepcopy(m)
dimV=len(m)

#a
def a(m):
    for diag in range(dimV):
        pivot = m[diag][diag]
        for col in range (dimV+1):
            m[diag][col]/=pivot
        for lin in range(diag+1, dimV):
            pivot2 = m[lin][diag]
            for col in range(diag, dimV+1):
                m[lin][col] -= m[diag][col] * pivot2
                
    return m

#print("Tabela: ",a(m))

#b
def solucao(m):
    m=a(m)
    for diag in range(dimV-1, -1, -1):
        for lin in range(diag-1, -1, -1):
            factor=m[lin][diag]
            for col in range(dimV, diag-1, -1):
                m[lin][col]-=m[diag][col]*factor
    return m

#print("Solucao do sistema: ",solucao(m))
    
#c
    
"""
A*dx=db-dA*x

db-daA*x =    
[0.3,0.3,0.3,0.3]-[[0.3,0.3,0.3,0.3],[0.3,0.3,0.3,0.3],[0.3,0.3,0.3,0.3],[0.3,0.3,0.3,0.3]]*[0.97263,-3.06443,0.32662,1.82038]
= [0.28344,0.28344,0.28344,0.28344]
"""

def externa():
    m=[[0.1,0.5,3,0.25,0.28344],[1.2,0.2,0.25,0.2,0.28344],[-1,0.25,0.3,2,0.28344],[2,0.00001,1,0.4,0.28344]]
    return solucao(m)

print("Estabilidade externa: ",externa())
    