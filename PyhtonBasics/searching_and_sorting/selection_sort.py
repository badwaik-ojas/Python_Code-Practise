def selection_sort(arr):
    l = len(arr)
    for i in range(l-1):
        min_index = i
        for j in range(i+1, l):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

arr = [20, 50, 70, 10, 5, 100, 2, 1, -100]
print(selection_sort(arr))
