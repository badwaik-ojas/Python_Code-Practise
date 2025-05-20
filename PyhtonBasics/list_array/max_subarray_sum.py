'''
Maximum Subarray Sum

Given an array arr of length n, consisting of integers, find the sum of the subarray (including an empty subarray) that has the maximum sum among all possible subarrays.

Input: arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: The subarray [4, -1, 2, 1] has the maximum sum 6.
'''
def max_subarray_sum(arr):
    if not arr:
        return 0     

    max_sum = arr[0]
    current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum