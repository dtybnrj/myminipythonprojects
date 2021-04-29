def bubble_sorting(a):
    n= len(a)
    count=0
    for i in range(n):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
                count=count+1
    print(count)


a= [8,22,7,9,31,19,5,13]
bubble_sorting(a)
for i in a:
    print(i)