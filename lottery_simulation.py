# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 18:18:30 2019

@author: adity
"""
import matplotlib.pyplot as plt
import random
x=[]
y=[]
account=0
for i in range(365):
    bet=random.randint(1,10)
    lucky_draw=random.randint(1,10)
    x.append(i+1)
    print("Bet:",bet)
    print("lucky draw:",lucky_draw)
    if bet==lucky_draw:
        account=account+900-100
        print("you win, account balance is:",account)
    else:
        account=account-100
        print("you lose, account balance is:",account)
    y.append(account)
plt.plot(x,y)
plt.show()