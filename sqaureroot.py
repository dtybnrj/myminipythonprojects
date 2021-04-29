# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 16:53:26 2019

@author: adity
"""

import math
d=[int(i) for i in input().split(',')]

C=50
H=30
Q=[]
for D in d:
    q=math.sqrt((2*C*D)/H)
    Q.append(round(q))
    x=[str(arr) for arr in Q]
print(','.join(x),end="")