'''
plus_one

You are given a large integer represented as an integer array digits, where each digits[i] is the i-th digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading zeroes.

Write a function to increment the large integer by one and return the resulting array of digits.

Input: digits = [1, 2, 3]
Output: [1, 2, 4]
 
Input: digits = [4, 3, 2, 1]
Output: [4, 3, 2, 2]
 
Input: digits = [9, 9, 9]
Output: [1, 0, 0, 0]
'''

def plus_one(digits):
    n = len(digits)

    for i in range(n-1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits
digits = [1, 2, 3]
print(plus_one(digits))
