'''
Max Consecutive Ones

Given a binary array nums, return the maximum number of consecutive 1s in the array.

Input: nums = [0, 0, 0, 0]
Output: 0
 
Input: nums = [1, 0, 1, 1, 0, 1, 1, 1, 1]
Output: 4
 
Input: nums = [1, 1, 0, 1, 1, 1]
Output: 3
'''

def find_max_consecutive_ones(nums):
    sum = 0
    m = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            sum += 1
            m = max(sum, m)
        else:
            sum = 0
    return m

nums = [1, 0, 1, 1, 0, 1, 1, 1, 1]
print(find_max_consecutive_ones(nums)) 
nums = [1, 1, 0, 1, 1, 1]
print(find_max_consecutive_ones(nums)) 
