'''
Rotate List

Given a list of integers and an integer D, write a function to rotate the list to the left by D positions.

Input: ARR = [1, 2, 3, 4, 5], D = 2
Output: [3, 4, 5, 1, 2]
 
Input: ARR = [10, 20, 30, 40, 50], D = 3
Output: [40, 50, 10, 20, 30]
 
Input: ARR = [7, 8, 9, 10], D = 1
Output: [8, 9, 10, 7]
'''
def rotate_left(ARR, D):
    n = len(ARR)
    d = D%n
    
    return ARR[d:] + ARR[:d]

ARR = [1, 2, 3, 4, 5]
D = 2
print(rotate_left(ARR, D))
