'''
Maximum difference between two consecutive elements in a list.
Find Maximum Difference Between Two Consecutive Elements (Brute Force Approach)

You are given a list of integers. Write a Python program to find the maximum difference between two consecutive elements in the list using a brute-force approach. The difference is defined as the absolute value of the difference between two consecutive elements.

Input: lst = [1, 7, 3, 10, 5]
Output: 7

The maximum difference is between 3 and 10 (i.e., |3 - 10| = 7).

Input: lst = [10, 11, 15, 3]
Output: 12

The maximum difference is between 15 and 3 (i.e., |15 - 3| = 12).

'''
def max_consecutive_difference(lst):
    # Your code goes here
    if len(lst) < 2:
        return 0
    
    max_diff = 0  # Initialize max difference as 0
    # Iterate through the list to calculate consecutive differences
    for i in range(1, len(lst)):
        current_diff = abs(lst[i] - lst[i - 1])  # Calculate absolute difference
        if current_diff > max_diff:  # Update max_diff if current_diff is greater
            max_diff = current_diff
    
    return max_diff  # Return the maximum difference