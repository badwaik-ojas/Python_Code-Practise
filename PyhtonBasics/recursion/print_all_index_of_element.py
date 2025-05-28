def print_all_index_of_element(arr, element, acc=0, temp=[]):
    if len(arr) == 0:
        if temp == []:
            return
        return temp
    if arr[0] == element:
        temp.append(acc)
    return print_all_index_of_element(arr[1:], element, acc + 1, temp)

print(print_all_index_of_element([1, 2, 3, 2, 4, 2], 2)) 