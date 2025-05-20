'''
Minimum in Rotated Sorted Array

Given a sorted array that has been rotated, find the minimum element in the array. The array was originally sorted in ascending order and then rotated at some pivot.

Input: nums = [4, 5, 6, 7, 0, 1, 2] 
Output: 0 
Explanation: The minimum element is 0.
 
Input: nums = [11, 13, 15, 17] 
Output: 11 
Explanation: The array was not rotated, and the minimum element is the first element.
'''

def min_in_rotated_sorted_arr(arr):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right)//2
        if arr[mid] > arr[right]:
            left = mid +1
        else:
            right = mid -1
    
    return arr[left]

nums = [11, 13, 15, 17] 
print(min_in_rotated_sorted_arr(nums))
