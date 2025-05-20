'''
Maximum Element in a List.

Given a list of integers, write a function to find the maximum element in the list.

Input: lst = [3, 5, 2, 9, 6]
Output: 9
 
Input: lst = [-1, -2, -3, -4]
Output: -1
 
Input: lst = [7]
Output: 7

'''
def find_max_element(lst):
    m = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > m:
            m = lst[i]
    return m
    
