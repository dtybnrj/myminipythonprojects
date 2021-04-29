def stone_paper_scissor(num1,num2,bit1,bit2):
    p1=int(num1[bit1])%3
    p2=int(num2[bit2])%3
    if player_one[p1]==player_two[p2]:
        print("Draw")
    elif player_one[p1]=='stone' and player_two[p2]=='scissor':
        print("player 1 wins")
    elif player_one[p1]=='stone' and player_two[p2]=='paper':
        print("player 2 wins")
    elif player_one[p1]=='paper' and player_two[p2]=='scissor':
        print("player 1 wins")
    elif player_one[p1]=='paper' and player_two[p2]=='stone':
        print("player 2 wins")
    elif player_one[p1]=='scissor' and player_two[p2]=='paper':
        print("player 1 wins")
    elif player_one[p1]=='scissor' and player_two[p2]=='stone':
        print("player 2 wins")





player_one={0:'paper',1:'stone',2:'scissor'}
player_two={0:'stone',1:'paper',2:'scissor'}
while 1:
    num1=input("enter the choice,player 1")
    num2=input("enter the choice,player 2")
    bit1=int(input("enter the secret bit position, player 1"))
    bit2=int(input("enter the secret bit position, player 2"))
    stone_paper_scissor(num1,num2,bit1,bit2)
    ch=input("do you want to continue? y/n")
    if ch=='n':
        break