# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 14:10:50 2019

@author: adity
"""

import cv2

img=cv2.imread('pic_1.jpg')

clahe=cv2.createCLAHE()

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

enh_img=clahe.apply(gray_img)

cv2.imwrite('enhanced.img',enh_img)
print("done")