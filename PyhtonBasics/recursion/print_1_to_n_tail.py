'''
Print 1 to N using Recursion
Problem Description:

You are given a positive integer n. Your task is to return a list of integers from 1 to n using recursion.
Input: n = 5
Output: [1, 2, 3, 4, 5]
 
Input: n = 3
Output: [1, 2, 3]
'''

def print_1_to_n(n, current=1,acc=[]):
    if n < 0:
        return []
    elif n == 0:
        return acc
    acc.append(current)
    return print_1_to_n(n-1, current + 1, acc)
    
print(print_1_to_n(10))  # Output: [1, 2, 3, 4, 5]

def print_1_to_n_1(n):
    if n == 1:
        return [1]
    return print_1_to_n_1(n-1) + [n]

print(print_1_to_n_1(10))  # Output: [1, 2, 3, 4, 5]

