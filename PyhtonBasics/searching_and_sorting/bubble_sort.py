def bubble_sort(arr):

    l = len(arr)
    for i in range(l-1):
        swapped = False
        for j in range(l-1-i):
            if arr[j+1] < arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break
    
    return arr

arr = [20, 50, 70, 10, 5, 100, 2, 1, -100]
print(bubble_sort(arr))