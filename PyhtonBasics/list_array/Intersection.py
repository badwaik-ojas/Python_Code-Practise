'''
Intersection of two Lists

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique, and you may return the result in any order.

Input: nums1 = [1, 2, 3], nums2 = [4, 5, 6]
Output: []
 
Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
Output: [2]
 
Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
Output: [9, 4]
'''

def intersection(arr1, arr2):
    result = []
    seen = set()
    for i in arr1:
        seen.add(i)
    for i in arr2:
        if i in seen:
            result.append(i)
            seen.remove(i)

    return result

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersection(nums1, nums2))