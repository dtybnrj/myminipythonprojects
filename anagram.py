# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 20:46:12 2019

@author: adity
"""

str1=input("enter the first word")
str2=input("enter the second word")
print(sorted(str1))
print(sorted(str2))
if sorted(str1)==sorted(str2):
    print("these are anagram")
else:
    print("these arent anagram")
    
