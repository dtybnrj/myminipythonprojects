n=int(input())
dic={}
for i in range(1,n+1):
    dic[i]=i*i
    if dic[i]==n*n:
        print(dic)
