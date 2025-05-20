'''
Missing Number

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Input: nums = [3, 0, 1]
Output: 2
 
Input: nums = [0, 1]
Output: 2
 
Input: nums = [8, 7, 6, 4, 3, 2, 0, 1]
Output: 5
'''

def find_missing_number(nums):
    k = len(nums)
    sum = (k * (k + 1))/2
    temp_sum = 0
    for i in nums:
        temp_sum += i
    return sum - temp_sum

nums = [8, 7, 6, 4, 3, 2, 0, 1]
print(find_missing_number(nums))