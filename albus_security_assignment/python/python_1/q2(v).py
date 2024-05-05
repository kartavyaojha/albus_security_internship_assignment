def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    piv=arr[len(arr)//2]
    left=[x for x in arr if x<piv]
    right=[x for x in arr if x>piv]
    mid=[x for x in arr if x==piv]
    return quick_sort(left)+mid+quick_sort(right)

array=[64, 25, 35, 234, 2366]
print("Given array is", array)
sorted_array = quick_sort(array)
print("Sorted array is", sorted_array)