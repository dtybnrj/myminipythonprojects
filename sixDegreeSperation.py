# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 17:09:33 2019

@author: adity
"""

import networkx as nx
import numpy
g=nx.read_edgelist("facebook_combined.txt")
N=list(g.nodes())
spll=[]
for u in N:
    for v in N:
        if u != v:
            l=nx.shortest_path_length(g,u,v)
            print("the shortest path between",u,"and",v,"is",l)
            spll.append(l)
            
max_spl=max(spll)
min_spl=min(spll)
avg_spl=numpy.average(spll)

print("the average short lenght is",avg_spl)
print("the maximum short lenght is",max_spl)
print("the minimum short lenght is",min_spl)
    
