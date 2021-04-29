# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:38:00 2019

@author: adity
"""

import turtle
import random
turtle.bgcolor("black")
tur = turtle.Turtle()
lst_color=["white","blue","green","yellow",]

width=5
height=7
dot_distance=20

tur.setpos(-250,250)


def spiral(m,n):
    k=0 
    l=0
    f=0
    tur.color("white")
    '''
    where k is starting row index
    and l is starting colum index
    
    '''
    
    while(k<m and l<n):
        if f==1:
            tur.right(90)
        #for +ce of colum index
        for i in range(l,n):
            #print(a[k][i],end=" ")
            tur.forward(dot_distance)
         
        k+=1
        f=1
        
        tur.right(90)
        #for +ce of row index
        for i in range(k,m):
            tur.forward(dot_distance)
            #print(a[i][n-1],end=" ")
            
        
        n-=1
        
        tur.right(90)
        if(k<m):
            for i in range(n-1,l-1,-1):
                tur.forward(dot_distance)
                #print(a[m-1][i],end=" ")
                
            m-=1
            
        tur.right(90)
        if(l<n):
            for i in range(m-1,k-1,-1):
                tur.forward(dot_distance)
                #print(a[i][l],end=" ")
            l+=1
        

    
spiral(20,20)
    