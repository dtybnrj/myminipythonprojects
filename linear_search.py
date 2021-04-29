def linearsearch(n,x):
    element=[]
    for i in range(n+1):
        element.append(i)

    flag=0
    for i in element:
        if i==x:
            print("we found the no."+str(i))
            flag=1


    if flag==0:
        print("no. not found")

linearsearch(1000,50)