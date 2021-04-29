# this code is for searching the same number in two list and giving there index value
n=int(input())
a=[int(i) for i in input().split()]
if n == len(a):
    j=(int(input()))-1
    b = a.copy()
    b.sort()
    i = 0
    while(i<=n):
        if a[j] == b[i]:
            print("{}".format(i+1), end="")
            break
        else:
            i = i+1
else:
    print("not in limit")



