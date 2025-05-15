'''
You are given an integer n. Your task is to return a right-angled triangle pattern where each row contains repeated digits. The first row contains the number 1 repeated once, the second row contains the number 2 repeated twice, and so on until the nth row contains the number n repeated n times.

Input: 5
Output: ['1', '22', '333', '4444', '55555']
 
Input: 3
Output: ['1', '22', '333']
'''
def generate_number_triangle(n):
    """
    Function to return a right-angled triangle of repeated numbers of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    lst = []
    for i in range(1, n+1):
        lst.append(str(i)*i)
    return lst

print(generate_number_triangle(3))