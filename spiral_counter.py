# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 11:25:35 2019

@author: adity
"""

def spiral(m,n,a):
    k=0
    l=0
    '''
    k is the starting index of row
    l is starting index of colume
    '''
    while(k<m and l<n):
        
        for i in range(k,m):
            print(a[i][l],end=" ")
        
        l+=1
        
        for i in range(l,n):
            print(a[m-1][i],end=" ")
            
        m-=1
        
        if(k<m):
            for i in range(m-1,k-1,-1):
                print(a[i][n-1],end=" ")
            n-=1    
            
        
        if(l<n):
            for i in range(n-1,l-1,-1):
                print(a[k][i],end=" ")
            k+=1
            
n=int(input())
m=n
a=[[j for j in input().split()] for i in range(n)]  
print(a)          
spiral(m,n,a)
        
        