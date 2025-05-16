'''
You are given the speed of a vehicle and the time it has traveled. Your task is to compute and return the distance traveled by the vehicle.

Formula:

To calculate the distance traveled by a vehicle:

Distance=Speed×Time

Input: speed = 60, time = 2
Output: 120.0
 
Input: speed = 50.5, time = 1.5
Output: 75.75
'''

def calculate_distance(speed, time):
    """
    Function to calculate the distance traveled by a vehicle.
    
    Parameters:
    speed (float): The speed of the vehicle.
    time (float): The time the vehicle has traveled.
    
    Returns:
    float: The distance traveled by the vehicle.
    """
    # Your code here
    return speed*time
