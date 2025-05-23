'''
Complex Number Class
Problem Description

Design a Python class named ComplexNumber to represent complex numbers and implement common methods to work with them. A complex number is a number of the form a+bia + bia+bi, where aaa is the real part and bbb is the imaginary part, and iii is the imaginary unit (i.e., −1\sqrt{-1}−1​).

Specifications

Constructor Method (__init__): Initialize two attributes, real and imaginary, representing the real and imaginary parts of the complex number.

Addition Method (add): Implement a method to add another ComplexNumber object to the current one. The result should be a new ComplexNumber object with the sum of the real and imaginary parts.

Subtraction Method (subtract): Implement a method to subtract another ComplexNumber object from the current one. The result should be a new ComplexNumber object with the difference of the real and imaginary parts.

Multiplication Method (multiply): Implement a method to multiply the current ComplexNumber object by another ComplexNumber object. The result should be a new ComplexNumber object with the product.

Comparison Method (__eq__): Implement a method to compare two ComplexNumber objects for equality. Two complex numbers are considered equal if both their real and imaginary parts are equal.

String Representation Method (__str__): Implement a method to return a string representation of the complex number in the format "a + bi".

Comparison with Python's Built-in Complex Class: After implementing the ComplexNumber class, compare its functionality with Python's built-in complex class. Show examples of addition, subtraction, multiplication, and division using both classes.

XX

python
Creating instances of ComplexNumber class
c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(1, 4)
 
# Testing the add method
print("Addition Result:", c1.add(c2))  # Output: "3 + 7i"
 
# Testing the subtract method
print("Subtraction Result:", c1.subtract(c2))  # Output: "1 - 1i"
 
# Testing the multiply method
print("Multiplication Result:", c1.multiply(c2))  # Output: "-10 + 11i"
 
# Testing the equality method
print("Equality Test:", c1 == ComplexNumber(2, 3))  # Output: True
 
# Comparison with Python's built-in complex class
py_c1 = complex(2, 3)
py_c2 = complex(1, 4)
 
print("Python Addition Result:", py_c1 + py_c2)  # Output: (3+7j)
print("Python Subtraction Result:", py_c1 - py_c2)  # Output: (1-1j)
print("Python Multiplication Result:", py_c1 * py_c2)  # Output: (-10+11j)
'''

class ComplexNumber:
    def __init__(self, real, imaginary):
        # Initialize real and imaginary parts
        self.real = real
        self.imaginary = imaginary
    
    def add(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
    
    def subtract(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    
    def multiply(self, other):
        real = (self.real * other.real) - (self.imaginary * other.imaginary)
        imaginary = (self.real * other.imaginary) + (self.imaginary * other.real)
        return ComplexNumber(real , imaginary)
        
    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary
        
    def __str__(self):
        if self.imaginary >= 0:
            return f"{self.real} + {self.imaginary}i"
        else:
            return f"{self.real} - {abs(self.imaginary)}i"
        
# Creating instances of ComplexNumber class
c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(1, 4)

# Testing the add method
print("Addition Result:", c1.add(c2))  # Output: "3 + 7i"

# Testing the subtract method
print("Subtraction Result:", c1.subtract(c2))  # Output: "1 - 1i"

# Testing the multiply method
print("Multiplication Result:", c1.multiply(c2))  # Output: "-10 + 11i"

# Testing the equality method
print("Equality Test:", c1 == ComplexNumber(2, 3))  # Output: True
