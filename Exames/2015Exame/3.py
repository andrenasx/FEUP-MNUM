# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 18:41:00 2020

@author: fmna
"""

import copy as c

m=[[1,0.5,1/3,-1],[0.5,1/3,1/4,1],[1/3,1/4,1/5,1]]
r=[0,0,0]
mc=c.deepcopy(m)
dimV=len(m)

"""a"""
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

#print(a(m))
    
"""b"""
def b(m):
    for diag in range(dimV-1, -1, -1):
        for lin in range(diag-1, -1, -1):
            factor=m[lin][diag]
            for col in range(dimV, diag-1, -1):
                m[lin][col]-=m[diag][col]*factor
    return m

#print(b(a(m)))

"""c"""

"""
A*dx=db-dA*x

db-daA*x =    
[0.05,0.05,0.05]-[[0.05,0.05,0.05],[0.05,0.05,0.05],[0.05,0.05,0.05]]*[-15,48,-30]
= [-0.1,-0.1,-0.1]
"""

#m=[[1,0.5,1/3,-0.1],[0.5,1/3,1/4,-0.1],[1/3,1/4,1/5,-0.1]]
#print(a(m))
#print("")
#print(b(m))
