# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 09:35:56 2019

@author: adity
"""

import networkx as nx
import random
import matplotlib.pyplot as plt
def add_egdes():
    nodes=list(G.nodes())
    for s in nodes:
        for t in nodes:
            if s!=t:
                r=random.random()
                if r<=0.5:
                    G.add_edge(s,t)
    return G
def assign_points(G):
    nodes=list(G.nodes())
    p=[]
    for each in nodes:
        p.append(100)
        
    return p

def distribute_point(G,points):
    nodes=list(G.nodes())
    new_points=[]
    for i in range(len(nodes)):
        new_points.append(0)
        
    for n in nodes:
        out=list(G.out_edges(n))
        if len(out)==0:
            new_points[n]=new_points[n]+points[n]
        else:
            

def keep_distributing(G,points):
    while(1):
        new_points=distribute_points(G,points)
        print(new_points)
        points=new_points
        stop=input("press # if want to break press any key continue: ")
        if stop=='#':
            break
    return new_points         
    

G=nx.DiGraph()
G.add_nodes_from([i for i in range(10)])
G=add_egdes()
nx.draw(G,with_labels=True)
plt.show()
# points distrubution
points=assign_points(G)
# keep distributing points
final_points=keep_distibuting(G,points)
