# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 12:20:34 2019

@author: adity
"""

from PIL import Image
import numpy
hieght=100
width=300
arr=numpy.zeros([width,hieght,3],dtype=numpy.uint8)
arr[:,:100]=[255,233,123]
img=Image.fromarray(arr)
img.save('test.png')
c=Image.open('test.png')
c.show()