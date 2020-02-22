#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 19:10:17 2019

@author: exame
"""

import copy as c

m=[[0.000030,0.213472,0.332147,0.235262],[0.215512,0.375623,0.476625,0.127653],[0.173257,0.663257,0.625675,0.285321]]
sol1=[[1,0,0,-0.931614],[0,1,0,0.003901],[0,0,1,-0.705882]]
sol2=[[1,0,0,-0.674262],[0,1,0,0.053108],[0,0,1,-0.991431]]
mc = c.copy(m)
dimV=len(m)
r=[0,0,0]

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

#Estabilidade Interna
def residuos(m):
    for eq in range(dimV):
        for sol in range(dimV):
            r[eq] = r[eq] + mc[eq][sol]*m[sol][dimV]
        r[eq] = mc[eq][dimV] - r[eq]

        

    return r

print("Resolvido pela eliminação gaussiana:")
print(gauss(m))
print("")
print("Residuos sol 1:")
r=[0,0,0]
print(residuos(sol1))
print("")
print("Residuos sol 2:")
r=[0,0,0]
print(residuos(sol2))
