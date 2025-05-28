def binary_search(arr, target, start, end):
    if start > end:
        return -1
    
    mid = start + (end - start)//2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid+1, end)
    
arr = [12, 34, 23, 43, 54]

print(binary_search(arr, 23, 0, len(arr)))
print(binary_search(arr, 44, 0, len(arr)))
