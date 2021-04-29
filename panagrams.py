import string

y=[str(a) for a in input().split()]
x="".join(y)
low=x.lower()
word=[ch for ch in low]
word.sort()
char=[]
ltr=list(string.ascii_lowercase)
for i in word:
    if i not in char:
        char.append(i)


if char==ltr:
    print("YES",end="")
else:
    print("NO",end="")

