def binary_search(l,x,start,end):
    if start==end:
        if l[start]==x:
            return start
        else:
            return -1
    else:
        mid=int((start+end)/2)
        if l[mid]==x:
            return mid
        elif l[mid]>x:
            #for left half
            return binary_search(l,x,start,mid-1)
        else:
            #for right half
            return binary_search(l,x,mid+1,end)