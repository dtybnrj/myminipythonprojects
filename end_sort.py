# def end_sort(a):
#     n=len(a)
#     count = 0
#     for i in range(n):
#         for j in range(n-i-1):
#             if a[j]>a[j+1]:
#                 a.append(a[j])
#                 a.remove(a[j])
#                 count=count+1
#     print(count)
#     print(a)
#
#
# a=[int(i) for i in input().split()]
# end_sort(a)

arr = [int(x) for x in input().split()]
arr1 = sorted(arr)
count = 0
for i in range(len(arr)):
    if arr[i] == arr1[count]:
        count+=1
print(len(arr)-count)