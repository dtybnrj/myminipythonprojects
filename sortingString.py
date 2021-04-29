# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 15:09:32 2019

@author: adity
"""

str1=[str(i) for i in input().split(',')]
str2=[]
for ele in sorted(str1):
    str2.append(ele)
    
print(','.join(str2))
