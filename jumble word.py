import random
def choose():
    words=['tech','dad','number','joke','goa','python']
    pick=random.choice(words)
    return pick
def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled
def play():
    p1name=input('enter the name player1: ')
    p2name=input('enter the name player2: ')
    pp1=0
    pp2=0
    turn=0
    while(1):
        picked_word=choose()
        qn=jumble(picked_word)
        print(qn)
        #player1
        if turn%2==0:
            print("its your turn :",p1name)
            ans=input("enter your answer")
            if ans==picked_word:
                pp1=pp1+1
                print("correct your score is: ",pp1)
            else:
                print("sorry, incorrect answer")
            c=int(input("press 1 to continue and 0 to quit"))
            if c==0:
                print("thank you your score is",pp1)
                break
        #player2
        else:
            print("its your turn: ",p2name)
            ans=input("enter your answer")
            if ans==picked_word:
                pp2=pp2+1
                print("correct,your score is",pp2)
            else:
                print("sorry incorrect answer")
            c=int(input("to continue press 1 and 0 to quit"))
            if c==0:
                print("thankyou your scre is:",pp2)
                break
        turn=turn+1
play()

