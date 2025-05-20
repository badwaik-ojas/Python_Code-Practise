'''
Count negative numbers in a sorted matrix

You are given an m x n matrix grid where each row and column is sorted in non-increasing order. Your task is to return the number of negative numbers present in the matrix.

Input: grid = [[4, 3, 2, 1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]] 
Output: 7 
Explanation: There are 7 negative numbers in the matrix.
 
Input: grid = [[3, 2], [1, 0]] 
Output: 0 
Explanation: There are no negative numbers in the matrix.
'''

def count_neg_num_in_matrix(grid):
    m, n = len(grid), len(grid[0])
    row, col = m-1, 0
    count = 0

    while row >= 0 and col < n:
        if grid[row][col] < 0:
            count += n - col
            row -= 1
        else:
            col +=1
        
    return count

grid = [[4, 3, 2, 1], 
        [3, 2, 1, -1], 
        [1, 1, -1, -2], 
        [-1, -1, -2, -3],
        [-2, -3, -4, -5]]
print(count_neg_num_in_matrix(grid)) 

grid = [[3, 2], 
        [1, 0]]
print(count_neg_num_in_matrix(grid)) 



