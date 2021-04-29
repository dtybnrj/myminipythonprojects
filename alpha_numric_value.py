# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 13:23:43 2019

@author: adity
"""

def extractMax(ss):
    num,res=0,0
    for i in range(len(ss)):
        if ss[i]>='0' and ss[i]<='9':
            num=num*10+int(int(ss[i])-0)
        else:
            res=max(res,num)
            num=0
            
    return max(res,num)
        
    
n=input()
a=[ch for ch in n]
b="".join(a)
print(extractMax(b))