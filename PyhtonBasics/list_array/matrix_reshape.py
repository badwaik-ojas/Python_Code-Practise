'''
Reshape Matrix

In MATLAB, there is a handy function called reshape that reshapes a matrix of dimensions m x n into a new one with a different size r x c keeping its original data in row-traversing order.

You are given an m x n matrix mat and two integers r and c representing the number of rows and columns of the wanted reshaped matrix. The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with the given parameters is possible and legal, output the new reshaped matrix. Otherwise, output the original matrix.

Input: mat = [[1, 2], [3, 4]], r = 1, c = 4
Output: [[1, 2, 3, 4]]
 
Input: mat = [[1, 2], [3, 4]], r = 2, c = 4
Output: [[1, 2], [3, 4]]
'''

def matrix_reshape(mat, r, c):
    m, n = len(mat), len(mat[0])

    flatten = [col for row in mat for col in row]

    reshaped = [flatten[c*i:c*(i+1)] for i in range(r)]

    return reshaped

mat = [[1, 2], [3, 4]]
r = 1
c = 4
print(matrix_reshape(mat, 1, 4))


