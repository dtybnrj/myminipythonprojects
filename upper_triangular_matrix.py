n=int(input())
m=[[j for j in input().split()] for i in range(0,n)]
for i in range(0,n):
    for j in range(0,n):
        if i > j:
            print("0",end=" ")
        elif (j+1)==n:
            print(m[i][j],end="")
        else:
            print(m[i][j],end=" ")
    if i+1==n:
        print("",end="")
    else:
        print("")



