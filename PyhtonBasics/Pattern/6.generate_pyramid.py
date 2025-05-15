'''
You are given an integer n. Your task is to return a pyramid pattern of '*' where each side has n rows, represented as a list of strings. The pyramid is centered, with 1 star in the first row, 3 stars in the second row, and so on, increasing by 2 stars per row until the base row has 2n - 1 stars.

Input: 3
Output: ['  *  ', ' *** ', '*****']
 
Input: 5
Output: ['    *    ', '   ***   ', '  *****  ', ' ******* ', '*********']

'''
def generate_pyramid(n):
    """
    Function to return a pyramid pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows in the pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the pyramid.
    """
    # Your code here
    pattern = []
    for i in range(n):
        stars = '*' * (2 * i + 1)
        spaces = ' ' * (n - i - 1)
        pattern.append(spaces + stars + spaces)
    return pattern

print(generate_pyramid(3))
