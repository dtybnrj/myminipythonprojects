n=int(input())
x=[int(i) for i in input().split()]
l=x[::-1]
c=[sum(e) for e in zip(l,x)]
print(' '.join(map(str,c)),end="")
