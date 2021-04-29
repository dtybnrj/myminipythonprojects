x=[]
n=int(input())
for i in range(n):
    y=int(input())
    x.append(y)

x.sort()
print(" ".join(map(str,x)),end=" ")