'''
search_matrix

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.

The first integer of each row is greater than the last integer of the previous row.

Write a function that takes an integer target and returns True if target is in matrix, or False otherwise. You must solve this problem with a time complexity better than O(m * n).

Input: matrix = [[1, 3, 5, 7], 
                 [10, 11, 16, 20], 
                 [23, 30, 34, 60]], target = 13
Output: False
 
Input: matrix = [[1, 3, 5, 7], 
                 [10, 11, 16, 20], 
                 [23, 30, 34, 60]], target = 3
Output: True
'''

def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m*n-1

    while left <= right:
        mid =(left + right)//2
        mid_value = matrix[mid//n][mid%n]

        if mid_value == target:
            return True
        elif mid_value < target:
            left =mid+1
        else:
            right = mid-1
        
    return False

matrix = [[1, 3, 5, 7], 
                 [10, 11, 16, 20], 
                 [23, 30, 34, 60]]
target = 16
print(search_matrix(matrix, target))

