'''
You are given a positive integer num. Your task is to check whether num is a perfect square or not. A perfect square is an integer that is the square of an integer (e.g., 1, 4, 9, 16, ...). Return True if num is a perfect square, and False otherwise.

Input: num = 16
Output: True
 
Input: num = 14
Output: False
'''

def is_perfect_square(num):
    if num < 2:
        return True  # 0 and 1 are perfect squares

    left, right = 2, num // 2

    while left <= right:
        mid = (left + right) // 2
        square = mid * mid

        if square == num:
            return True
        elif square < num:
            left = mid + 1
        else:
            right = mid - 1

    return False

# Example usage:
print(is_perfect_square(16))  # Output: True
print(is_perfect_square(14))  # Output: False
