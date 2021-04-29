# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 17:44:48 2019

@author: adity
"""

    
n=[]
factorial=[]
for i in range(5):
    x=int(input())
    n.append(x)
    

for i in n:
    fac=1
    for j in range(1,i+1):
        if j==0:
            break
        fac=fac*j
    factorial.append(fac)
factorial.remove(factorial[0])
for i in factorial:
    print(i)