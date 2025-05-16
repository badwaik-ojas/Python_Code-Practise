'''
You are given a temperature in Celsius. Your task is to convert it to Fahrenheit and return the result.

Formula:

To convert Celsius to Fahrenheit, use the formula:

F = (9/5 * C) + 32

Where F is the temperature in Fahrenheit and C is the temperature in Celsius.

Input: C = 25
Output: 77.0
 
Input: C = 0
Output: 32.0
'''
def celsius_to_fahrenheit(C):
    """
    Function to convert temperature from Celsius to Fahrenheit.
    
    Parameters:
    C (float): The temperature in Celsius.
    
    Returns:
    float: The temperature in Fahrenheit.
    """

    return (9/5 * C) + 32
