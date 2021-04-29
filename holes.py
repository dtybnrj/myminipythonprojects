# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 11:11:27 2019

@author: adity
"""

n=list(input())
count=0
for i in n:
    if i=='A' or i=='O' or i=='P' or i=='Q' or i=='D' or i=='R':
        count+=1
    elif i=='B':
        count+=2
        
print(count,end="")