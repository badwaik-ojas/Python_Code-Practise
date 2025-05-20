'''
Reverse a List

Given a list of integers, write a function to reverse the order of elements in the list.

Input: lst = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
 
Input: lst = [10, 20, 30]
Output: [30, 20, 10]
 
Input: lst = [7, 8, 9]
Output: [9, 8, 7]
'''

def reverse_list(lst):
    k = len(lst)-1
    for i in range(len(lst)//2):
        lst[i], lst[k] = lst[k], lst[i]
        k -=1
    
    return lst

lst = [1, 2, 3, 4, 5]
print(reverse_list(lst))
 
lst = [10, 20, 30]
print(reverse_list(lst))