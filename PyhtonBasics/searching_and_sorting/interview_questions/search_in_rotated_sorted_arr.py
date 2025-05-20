'''
Search in Rotated Sorted Array

Given a sorted array that has been rotated, find the index of a given target value. The array was originally sorted in ascending order and then rotated at some pivot.

Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0 
Output: 4 
Explanation: The target value 0 is at index 4 in the rotated array.
 
 
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3 
Output: -1 
Explanation: The target value 3 is not present in the array.
'''

def search_in_rotated_sorted_arr(arr, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1  # Search left half
            else:
                left = mid + 1   # Search right half

        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1   # Search right half
            else:
                right = mid - 1  # Search left half

    return -1  # Target not found

nums = [4, 5, 6, 7, 0, 1, 2]
target = 0 
print(search_in_rotated_sorted_arr(nums, target))


