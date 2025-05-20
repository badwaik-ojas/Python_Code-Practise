'''
Rotate Image

You are given an n x n 2D matrix representing an image. Rotate the image by 90 degrees clockwise. The rotation should be done in-place, meaning you have to modify the input matrix directly without using any additional matrix for storage.

Input: matrix = [[5, 1, 9, 11],
                 [2, 4, 8, 10],
                 [13, 3, 6, 7],
                 [15, 14, 12, 16]]
Output: [[15, 13, 2, 5], 
         [14, 3, 4, 1],
         [12, 6, 8, 9],
         [16, 7, 10, 11]]
 
 
Input: matrix = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]
Output: [[7, 4, 1],
         [8, 5, 2],
         [9, 6, 3]]
'''

def rotate_image(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
    
    return matrix


matrix = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]
print(rotate_image(matrix))
