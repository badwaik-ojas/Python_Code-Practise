'''
You are given an integer n. Your task is to return a pyramid pattern of numbers, where each row contains increasing numbers starting from 1 up to the row number, and the pyramid is centered with leading spaces.

Input: 4
Output: ['   1   ', '  1 2  ', ' 1 2 3 ', '1 2 3 4']
 
Input: 3
Output: ['  1  ', ' 1 2 ', '1 2 3']
'''

def generate_number_pyramid(n):
    """
    Function to return a pyramid pattern of numbers of height n as a list of strings.
    
    Parameters:
    n (int): The height of the pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the pyramid pattern.

    """
    pattern = []
    space = ' '
    for i in range(1, n+1):
        st = [str(j) for j in range(1, i+1)]
        st1 = (n-i) * space + space.join(st) + (n-i) * space
        pattern.append(st1)

    return pattern

print(generate_number_pyramid(4))
        
            
            
            
        
         