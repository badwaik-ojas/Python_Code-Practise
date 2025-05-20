'''
Matrix obtained by Rotation or not?

You are given two n x n binary matrices mat and target. Your task is to determine whether it is possible to make mat equal to target by rotating mat in 90-degree increments (clockwise). You can rotate mat by 90, 180, or 270 degrees, or leave it unchanged.

Input: mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]], target = [[1, 1, 1], [0, 1, 0], [0, 0, 0]]
Output: True
 
Input: mat = [[0, 1], [1, 1]], target = [[1, 0], [0, 1]]
Output: False
'''
def findRotation(mat, target):
    for _ in range(4):
        print(mat)
        print("---")
        if mat == target:
            return True
        mat = rotate90(mat)
    return False

def rotate90(matrix):
    n = len(matrix)
    # Transpose and then reverse each row
    return [ [matrix[n - j - 1][i] for j in range(n)] for i in range(n) ]

mat = [[0, 0, 0], 
       [0, 1, 0], 
       [1, 1, 1]]
target = [[1, 1, 1], [0, 1, 0], [0, 0, 0]]
print(findRotation(mat, target))