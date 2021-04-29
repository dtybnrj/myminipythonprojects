# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 15:53:11 2019

@author: adity
"""

x=[int(i) for i in input().split()]
for i in x:
    if i==0:
        x.append(i)
        x.remove(i)
y=[str(i) for i in x]
print(" ".join(y),end="")