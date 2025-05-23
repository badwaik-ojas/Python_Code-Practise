'''
Spiral Matrix

You are given an m x n matrix. Write a function that returns all the elements of the matrix in spiral order, starting from the top-left corner, moving right across the top row, then down the last column, then left across the bottom row, and then up the first column, repeating this process until all the elements have been visited.

Input: matrix = [[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12]]
Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
 
Input: matrix = [[1, 2, 3], 
                 [4, 5, 6], 
                 [7, 8, 9]]
Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
'''

def spiral_order(matrix):
    result = []
    if not matrix:
        return result
    
    top, bottom = 0, len(matrix)-1
    left, right = 0, len(matrix[0])-1

    while top <= bottom and left <= right:
         
        for i in range(left, right+1):
            result.append(matrix[top][i])
        top += 1
         
        for j in range(top, bottom+1):
            result.append(matrix[j][right])
        right -= 1

        if top <= bottom:
            for i in range(right, -1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top-1, -1):
                result.append(matrix[i][left])
            left += 1

    return result

matrix = [[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12]]
print(spiral_order(matrix))
            


