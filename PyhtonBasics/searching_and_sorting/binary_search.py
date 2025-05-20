def binary_search(arr, target):
    end = len(arr)-1
    start = 0

    while start <= end:

        mid = (end+start)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return -1

arr = [12, 14, 16, 18, 20, 80, 90, 140, 145]
print(binary_search(arr, 80))
print(binary_search(arr, 13))

