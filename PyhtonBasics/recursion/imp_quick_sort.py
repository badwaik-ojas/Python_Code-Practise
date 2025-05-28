def quick_sort_helper(arr, start, end):
    if start >= end:
        return
    
    pivot = partition(arr, start, end)

    quick_sort_helper(arr, start, pivot-1)
    quick_sort_helper(arr, pivot+1, end)

    return arr

def partition(arr, start, end):

    i = start
    pivot = arr[end]

    for j in range(start, end):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[end] = arr[end], arr[i]
    return i

def quick_sort(arr):
    return quick_sort_helper(arr, 0, len(arr)-1)

arr = [12, 44, 7, 8, 90, 90, 111, 2, 50]
print(quick_sort(arr))

