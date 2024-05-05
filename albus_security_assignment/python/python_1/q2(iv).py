def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    res = merge(left, right)
    return res

def merge(left, right):
    merged=[]
    left_index=0
    right_index=0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index+=1
    merged+=left[left_index:]
    merged+=right[right_index:]
    return merged

array=[64, 25, 35, 234, 2366]
print("Given array is", array)
sorted_array = merge_sort(array)
print("Sorted array is", sorted_array)