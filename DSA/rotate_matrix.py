def rotate(mat):
    length = len(mat)
    for i in range(length):
        for j in range(i, length):
            mat[j][i], mat[i][j] = mat[i][j], mat[j][i]

    print(mat)
    transposed_mat = []
    for row in mat:
        transposed_mat.append(row[::-1])

    return transposed_mat
    

mat = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(mat=mat))








