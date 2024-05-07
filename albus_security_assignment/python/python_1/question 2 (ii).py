def binary_search(array,n,x):
    low=0
    high=n-1
    mid=0

    while low<=high:
        mid = int(low + ((high-low)/2))
        if array[mid]<x :
            low=mid+1
        elif array[mid]>x:
            high=mid-1
        else:
            return mid
    return -1
array = [2, 4, 0, 6, 1, 9, 8]
x=9
n=len(array)
print("The index of",x,"is",binary_search(array,n,x))