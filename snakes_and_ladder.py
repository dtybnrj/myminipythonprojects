# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from PIL import Image
import random
end=100
def show_board():
    img = Image.open('Screenshot (6).png')
    img.show()
    
def check_ladder(points):
    if points==8:
        print('ladder')
        return 26
    elif points==21:
        print('ladder')
        return 82
    elif points==43:
        print('ladder')
        return 77
    elif points==50:
        print('ladder')
        return 91
    elif points==54:
        print('ladder')
        return 93
    elif points==62:
        print('ladder')
        return 96
    elif points==66:
        print('ladder')
        return 87
    elif points==80:
        print('ladder')
        return 100
    else:
        return points
    
def check_snake(points):
    if points==98:
        print('snake')
        return 28
    elif points==95:
        print('snake')
        return 24
    elif points==92:
        print('snake')
        return 51
    elif points==83:
        print('snake')
        return 19
    elif points==73:
        print('snake')
        return 1
    elif points==64:
        print('snake')
        return 36
    elif points==69:
        print('snake')
        return 9
    elif points==59:
        print('snake')
        return 17
    elif points==55:
        print('snake')
        return 7
    elif points==52:
        print('snake')
        return 11
    elif points==44:
        print('snake')
        return 22
    elif points==46:
        print('snake')
        return 5
    elif points==48:
        print('snake')
        return 9
    else:
        return points
    
def reached_end(points):
    if points==end:
        return True
    else:
        return False
    

def play():
    p1name = input('enter your name player1')
    p2name = input('ebter your name player2')
    pp1=0
    pp2=0
    turn=0
    while(1):
        if turn%2==0:
            print('its your turn',p1name)
            c = int(input('to continue press 1,for quite press 0'))
            if c==0:
                print(p1name,'scored',pp1)
                print(p2name,'scored',pp2)
                break
            dice=random.randint(1,6)
            print('dice showed:',dice)
            pp1=pp1+dice
            pp1=check_ladder(pp1)
            pp1=check_snake(pp1)
            
            if pp1>end:
                pp1=end
            print(p1name,'scored',pp1)
            
            if reached_end(pp1):
                print(p1name,'won')
        else:
            print('its your turn',p2name)
            c = int(input('to continue press 1,for quite press 0'))
            if c==0:
                print(p1name,'scored',pp1)
                print(p2name,'scored',pp2)
                break
            dice=random.randint(1,6)
            print('dice showed:',dice)
            pp2=pp2+dice
            pp2=check_ladder(pp2)
            pp2=check_snake(pp2)
            
            if pp2>end:
                pp2=end
            print(p2name,'scored',pp2)
            
            if reached_end(pp2):
                print(p2name,'won')
        turn=turn+1
        
show_board()
play()