# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 10:47:10 2019

@author: adity
"""

n=input()
x=[ch for ch in n]
y=[]
for i in x:
    if ord(i)>=33 and ord(i)<=47 or ord(i)==64:
        y.append(ord(i))
        
    elif ord(i)==32:
        print("NO",end="")
        break
for j in y:
    if j>=33 and j<=47 or j==64:
        print("YES",end="")
        break