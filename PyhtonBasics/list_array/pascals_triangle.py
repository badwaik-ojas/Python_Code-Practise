'''
Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle. In Pascal's triangle, each number is the sum of the two numbers directly above it. The first row is row 0, which is [1].

Input: numRows = 3
Output: [
  [1],
  [1, 1],
  [1, 2, 1]
]
 
Input: numRows = 1
Output: [
  [1]
]
 
Input: numRows = 5
Output: [
  [1],
  [1, 1],
  [1, 2, 1],
  [1, 3, 3, 1],
  [1, 4, 6, 4, 1]
]

'''

def pascals_triangle(num_row):
    l1 = []
    for i in range(1, num_row+1):
        l2 = []
        k = 1
        while k <= i and i in [1, 2]:
            l2.append(1)
            k += 1
        if i >=3:
            for j in range(i):
                if j in [0, i-1]:
                    l2.append(1)
                elif j > 0 and j<i-1:
                    l2.append(l1[i-2][j-1] + l1[i-2][j])
        l1.append(l2)
    return l1

print(pascals_triangle(5))

def pascals_triangle_1(num_row):
    l1 = []
    for i in range(num_row):
        l2 = [1] * (i+1)
        for j in range(1, i):
            l2[j] = l1[i-1][j-1] + l1[i-1][j]
        
        l1.append(l2)
        
    return l1

print(pascals_triangle_1(5))
