#[12, 25, 11, 34, 90, 22]

def insertion_sort(arr):
    l = len(arr)
    for i in range(1, l):
        current = arr[i]
        j = i-1
        while j >=0 and arr[j] > current:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = current
    return arr

arr = [20, 50, 70, 10, 5, 100, 2, 1, -100]
print(insertion_sort(arr))