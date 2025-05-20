'''
Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, and an integer target, find the starting and ending position of the given target value. If target is not found in the array, return [-1, -1].

Input: nums = [5, 7, 7, 8, 8, 10], target = 8 
Output: [3, 4] 
Explanation: The target 8 appears from index 3 to index 4.
 
 
Input: nums = [5, 7, 7, 8, 8, 10], target = 6 
Output: [-1, -1] 
Explanation: The target 6 is not found in the array.
'''

def first_last_position_array(arr, target):
    def find_first():
        left, right = 0, len(arr)-1
        first = -1
        while left <= right:
            mid = (left + right)//2
            if arr[mid] == target:
                first = mid
                right = mid - 1
            elif arr[mid] > target:
                right = mid - 1
            else:
                left = left + 1
        return first
    
    def find_last():
        left, right = 0, len(arr) -1
        last = -1
        while left <= right:
            mid = (left + right)//2
            if arr[mid] == target:
                last = mid
                left = mid + 1
            elif arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return last
    
    return [find_first(), find_last()]

nums = [5, 7, 7, 8, 8, 10]
target = 8 

print(first_last_position_array(nums, target))
            

