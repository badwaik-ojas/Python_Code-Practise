def linear_search(arr, value):
    length = len(arr)
    for i in range(0, length):
        if arr[i] == value:
            return i
    
    return -1

arr = [9, 18, 27, 36]
print(linear_search(arr, 18))
print(linear_search(arr, 20))