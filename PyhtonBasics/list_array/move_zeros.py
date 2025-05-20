'''
Move Zeroes

Given an integer array nums, write a function to move all 0s to the end of the array while maintaining the relative order of the non-zero elements.

Input: nums = [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]
 
Input: nums = [0, 0, 1]
Output: [1, 0, 0]
 
Input: nums = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
Output: [4, 2, 4, 3, 5, 1, 0, 0, 0, 0]
'''

def move_zeros(arr):
    index = 0
    for i in arr:
        if i!=0:
            arr[index]=i
            index += 1
    
    while index < len(arr):
        arr[index] = 0
        index += 1
    return arr
nums = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
print(move_zeros(nums))
