def magic_square(n):
    magicSqaure=[]

    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        magicSqaure.append(l)
    i=n//2
    j=n-1

    num=n*n
    count=1
    while count <= num:
        if i == -1 and j == n:
            j=n-2
            i=0
        else:
            if j==n:
                j=0
            if i<0:
                i=n-1


        if magicSqaure[i][j]!=0:
            j=j-2
            i=i+1
            continue
        else:
            magicSqaure[i][j] = count
            count += 1

        i=i-1
        j=j+1


    for i in range(n):
        for j in range(n):
            print(magicSqaure[i][j],end=" ")
        print()
    print("the sum of rows, columns and diagonal: "+str(n*(n**2+1)/2))

c=int(input())

magic_square(c)


