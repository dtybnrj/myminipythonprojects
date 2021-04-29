def isVowel(c):
    return (c=='a') or (c=='e') or (c=='i') or (c=='o') or (c=='u')

def removeVowels(str):
    print(str[0],end="")
    for i in range(1,len(str)):
        if (isVowel(str[i-1])!=True) or (isVowel(str[i])!=True):
            print(str[i],end="")


x=[str(a) for a in input().split()]
y=" ".join(x)
removeVowels(y)