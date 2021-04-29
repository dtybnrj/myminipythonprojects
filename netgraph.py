# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 17:56:23 2019

@author: adity
"""

import networkx as nx
import matplotlib.pyplot as plt
G=nx.gnp_random_graph(50,0.3)
nx.draw(G)
plt.show()