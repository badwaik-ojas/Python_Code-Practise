'''
Is Array Sorted?

Write a function that checks whether the given array is sorted in non-decreasing order. The array is considered sorted if every element is less than or equal to the next element.

arr = [5, 4, 3, 2, 1]
 False
 
arr = [1, 3, 2, 4, 5]
 False
 
arr = [1, 2, 3, 4, 5]
 True

'''
def is_arr_sorted(arr):
    l = len(arr)-1
    for i in range(0, l-1):
        if arr[i] > arr[i+1]: 
            return False
    return True

arr = [5, 4, 3, 2, 1]
print(is_arr_sorted(arr)) 
arr = [1, 3, 2, 4, 5]
print(is_arr_sorted(arr))  
arr = [1, 2, 3, 4, 5]
print(is_arr_sorted(arr)) 

