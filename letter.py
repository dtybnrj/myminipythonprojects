# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 11:51:43 2019

@author: adity
"""

lis_input=list(input())

upper_count=0
lower_count=0

for i in lis_input:
    if i.isupper():
        upper_count+=1
    elif i.islower():
        lower_count+=1
print(upper_count,lower_count)