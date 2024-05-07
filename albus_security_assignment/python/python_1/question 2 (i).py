def linear_search(array,n,x):
    for i in range(n):
        if array[i] == x:
            return i
    return -1

array = [2, 4, 0, 6, 1, 9]
x = 6
n = len(array)
result = linear_search(array, n, x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)