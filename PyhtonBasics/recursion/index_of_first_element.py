def index_of_first_element(arr, element, acc=0):
    if len(arr) == 0:
        return -1
    if arr[0] == element:
        return acc
    return index_of_first_element(arr[1:], element, acc + 1)

print(index_of_first_element([1,2,3,4,3,2], 4)) 

def find_first_index(arr, element):
    def helper(index):
        if index == len(arr):
            return -1
        if arr[index] == element:
            return index
        else:
            return helper(index + 1)
    return helper(0)

print(find_first_index([1,2,3,4,3,2], 4))
