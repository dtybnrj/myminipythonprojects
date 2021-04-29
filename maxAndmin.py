x = input()
num = list(map(int, x.split()))
l =[]
for i in num:
    if i%3 != 0:
        l.append(i)
print(*l, sep = " ",end="")