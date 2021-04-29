# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 11:25:57 2019

@author: adity
"""
import sys
x=[int(j) for j in input().split()]
n=x[0]
m=x[1]
y=[int(i) for i in input().split()]
z=[]


if n==len(y):
    y.sort()
    min_diff=sys.maxsize
    first=0
    last=0
    i=0
    while(i+m-1<n):
        diff=y[i+m-1]-y[i]
        if diff<min_diff:
            min_diff=diff
            first=i
            last=i+m-1
                
        i+=1
        q=(y[last]-y[first])
        z.append(q)
    print(min(z),end="")
        
             
else:
    print("limit exceed")
        
