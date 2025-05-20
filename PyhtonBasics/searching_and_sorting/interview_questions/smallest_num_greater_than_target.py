'''
Find smallest letter greater than target

You are given a sorted array of characters letters, sorted in non-decreasing order, and a character target. There are at least two different characters in letters. Your task is to return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

Input:
letters = ['c', 'f', 'j']
target = 'k'
Output: 'c'
 
Input:
letters = ['c', 'f', 'j']
target = 'c'
Output: 'f'
 
Input:
letters = ['c', 'f', 'j']
target = 'a'
Output: 'c'

'''

def smallest_num_greater_than_target(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left +right)//2
        if arr[mid] > target:
            right = right -1
        else:
            left = left +1
    
    return arr[left % len(arr)]

letters = ['c', 'f', 'j']
target = 'k'
print(smallest_num_greater_than_target(letters, target))
 
letters = ['c', 'f', 'j']
target = 'c'
print(smallest_num_greater_than_target(letters, target))
 
letters = ['c', 'f', 'j']
target = 'a'
print(smallest_num_greater_than_target(letters, target))