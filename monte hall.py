from random import *
door=[0]*3
goatdoor=[0]*2
swap=0
dont_swap=0
j=0
while j<10:
    x=randint(0,2)
    door[x]="BMW"
    for i in range(0,3):
        if i==x:
            continue
        else:
            door[i]="goat"
            goatdoor.append(i)
    chce=int(input("enter the number"))
    door_open=choice(goatdoor)
    while door_open==chce:
        door_open=choice(goatdoor)
    ch=input("do you want to continue? y/n")
    if ch=='y':
        if door[chce]=='goat':
            print("player wins")
            swap=swap+1
        else:
            print("player lost")
    else:
        if door[chce]=='goat':
            print("player lost")
        else:
            print("player wins")
            dont_swap=dont_swap+1
    j=j+1


print(swap)
print(dont_swap)
