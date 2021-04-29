# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 12:15:31 2019

@author: adity
"""

def spiral(m,n,a):
    k=0 
    l=0
    '''
    where k is starting row index
    and l is starting colum index
    
    '''
    while(k<m and l<n):
        #for +ce of colum index
        for i in range(l,n):
            print(a[k][i],end=" ")
            
        k+=1
        #for +ce of row index
        for i in range(k,m):
            print(a[i][n-1],end=" ")
            
        n-=1
        if(k<m):
            for i in range(n-1,l-1,-1):
                print(a[m-1][i],end=" ")
                
            m-=1
        if(l<n):
            for i in range(m-1,k-1,-1):
                print(a[i][l],end=" ")
            l+=1

a=[]
count=1
for i in range(4):
    l=[]
    for j in range(4):
        l.append(count)        
        count+=1
    a.append(l)
    
spiral(4,4,a)
            
        
        
    
    