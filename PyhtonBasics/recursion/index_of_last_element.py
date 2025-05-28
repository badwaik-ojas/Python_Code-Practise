def index_of_last_element(arr, element, acc=0, temp=-1):
    if len(arr) == 0:
        if temp == -1:
            return
        return temp
    if arr[0] == element:
        temp = acc
    return index_of_last_element(arr[1:], element, acc + 1, temp)

print(index_of_last_element([1,2,3,4,3,2], 5)) 