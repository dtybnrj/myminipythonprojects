# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
#
# c=int(input())
# factorial(c)
# print(factorial(c))


k = int(input())

fac = 1
for i in range(1,k+1):
    if(k==0):
        break
    fac=fac*i

print(fac)