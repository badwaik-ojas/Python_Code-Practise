def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    merge_sort_helper(arr, 0, len(arr)-1)
    return arr

def merge_sort_helper(arr, s, e):
    if s>=e:
        return
    
    mid = s + (e-s)//2

    merge_sort_helper(arr, s, mid)
    merge_sort_helper(arr, mid+1, e)

    sort(arr, s, mid, e)
    return

def sort(arr, s, mid, e):
    i = s
    j = mid+1

    temp = []

    while i <= mid and j<= e:
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i += 1
        elif arr[i] > arr[j]:
            temp.append(arr[j])
            j += 1
        elif arr[i] == arr[j]:
            temp.append(arr[j])
            temp.append(arr[j])
            j += 1
            i += 1
        
    while i <= mid:
        temp.append(arr[i])
        i +=1

    while j <= e:
        temp.append(arr[j])
        j +=1

    startoftemp = 0
    startofarr = s

    while startofarr <=e:
        arr[startofarr] = temp[startoftemp]
        startofarr += 1
        startoftemp += 1
    return

arr = [12, 1, 34, 22, 22, 45, 7]
merge_sort(arr)
print(arr)