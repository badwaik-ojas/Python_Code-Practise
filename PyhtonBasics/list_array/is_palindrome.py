'''
Palindrome List

Given a list of integers, determine if it is a palindrome. A list is considered a palindrome if it reads the same forward and backward.

Input: lst = [7, 8, 9, 8, 7]
Output: True
 
Input: lst = [1, 2, 3, 4, 5]
Output: False
 
Input: lst = [1, 2, 3, 2, 1]
Output: True
'''

def is_palindrome(lst):
    k = len(lst)-1
    for i in range(len(lst)//2):
        if lst[i] != lst[k]:
            return False
        k -=1
    return True

lst = [7, 8, 9, 8, 7]
print(is_palindrome(lst))
 
lst = [1, 2, 3, 4, 5]
print(is_palindrome(lst))
 
lst = [1, 2, 3, 2, 1]
print(is_palindrome(lst))