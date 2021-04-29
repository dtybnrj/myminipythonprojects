# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 12:07:35 2019

@author: aditya
"""
def removeDuplicate(li):
    newli=[]
    seen=set()
    for item in li:
        if item not in seen:
            seen.add(item)
            newli.append(item)
    arr=[str(a) for a in newli]

    print(" ".join(arr),end="")



li=[int(i) for i in input().split()]

removeDuplicate(li)
