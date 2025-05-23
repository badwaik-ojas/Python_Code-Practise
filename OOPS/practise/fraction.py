'''
Fraction Class
Problem Description

Problem Title: Implement a Fraction Class

Design a Python class named Fraction to represent and manipulate mathematical fractions. The class should support basic arithmetic operations and comparisons.

Specifications:

Constructor Method (__init__):

Initialize the fraction with two attributes: numerator and denominator.

Ensure that the denominator is not zero. If zero is provided, raise a ValueError.

Methods:

add(self, other): Add another Fraction object to the current fraction.

subtract(self, other): Subtract another Fraction object from the current fraction.

multiply(self, other): Multiply the current fraction by another Fraction object.

divide(self, other): Divide the current fraction by another Fraction object. If the other fraction's numerator is zero, raise a ValueError for division by zero.

__eq__(self, other): Check if two Fraction objects are equal.

__str__(self): Return a string representation of the fraction in the form numerator/denominator.

__repr__(self): Return a detailed string representation for debugging.

Simplify Fractions:

Ensure that fractions are always stored in their simplest form. Use a basic method to find the greatest common divisor (GCD) and simplify the fraction. Avoid recursion and imported functions.

Example:

Creating instances of the Fraction class
frac1 = Fraction(1, 2)
frac2 = Fraction(3, 4)
 
# Testing the add method
print(frac1.add(frac2))  # Output: 5/4
 
# Testing the subtract method
print(frac1.subtract(frac2))  # Output: -1/4
 
# Testing the multiply method
print(frac1.multiply(frac2))  # Output: 3/8
 
# Testing the divide method
print(frac1.divide(frac2))  # Output: 2/3
print(frac1.divide(Fraction(0, 1)))  # Output: Error: Cannot divide by zero
 
# Testing equality
print(frac1 == Fraction(2, 4))  # Output: True
 
# Testing string representation
print(frac1)  # Output: 1/2
'''

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.numerator = numerator
        self.denominator = denominator
        self._simplify()

    def _gcd(self, a, b):
        # Iterative method to find GCD
        while b != 0:
            a, b = b, a % b
        return abs(a)

    def _simplify(self):
        gcd = self._gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

        # Ensure the denominator is positive
        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1

    def add(self, other):
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def subtract(self, other):
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def multiply(self, other):
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def divide(self, other):
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero.")
        num = self.numerator * other.denominator
        den = self.denominator * other.numerator
        return Fraction(num, den)

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"Fraction(numerator={self.numerator}, denominator={self.denominator})"

frac1 = Fraction(1, 2)
frac2 = Fraction(3, 4)

# Add
print("Addition:", frac1.add(frac2))         # Output: 5/4

# Subtract
print("Subtraction:", frac1.subtract(frac2)) # Output: -1/4

# Multiply
print("Multiplication:", frac1.multiply(frac2)) # Output: 3/8

# Divide
print("Division:", frac1.divide(frac2))      # Output: 2/3

# Division by zero check
try:
    print("Division by zero:", frac1.divide(Fraction(0, 1)))
except ValueError as e:
    print("Error:", e)

# Equality
print("Equality check:", frac1 == Fraction(2, 4))  # Output: True

# String Representation
print("String format:", frac1)  # Output: 1/2

# Detailed representation for debugging
print("Debug info:", repr(frac1))  # Output: Fraction(numerator=1, denominator=2)
