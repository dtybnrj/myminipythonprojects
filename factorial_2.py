def factorial(n):
    product=1
    for i in range(1,n+1):
        product=product*i
    return product

n=int(input("Enter the value for its factorial: "))
if n<0:
    print("Number is negative so it's factorial can't be find out")
else:
    c=factorial(n)
    print("the factorial of",n,"is",c)