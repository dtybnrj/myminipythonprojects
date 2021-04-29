# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 11:37:56 2019

@author: adity
"""

word=list(input())
length=len(word)

def palindrome(word,length):
    i=0
    j=length-1
    while i<=j:
        if word[i]==word[j]=='.':
            word[i]=word[j]='a'
        elif word[i] != word[j]:
            if word[i]=='.':
                word[i]=word[j]
            elif word[j]=='.':
                word[j]=word[i]
            else:
                return -1
        i+=1
        j-=1
    return (''.join(word))
print(palindrome(word,length))