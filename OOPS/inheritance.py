'''
Inheritance allows a class (called the child or subclass) to inherit attributes and methods from another 
class (called the parent or superclass). 
This promotes code reusability and establishes a natural hierarchy between classes.
'''

class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}.")

# Inherit from Parent class
class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call the constructor of the Parent class
        self.age = age

    def introduce(self):
        print(f"I am {self.name} and I am {self.age} years old.")

# Create an instance of Child
child = Child("Alice", 10)

# Access methods from both Child and Parent classes
child.greet()       # Output: Hello, my name is Alice.
child.introduce()   # Output: I am Alice and I am 10 years old.

'''
Method Overriding

Accessing Parent Methods
    class Child(Parent):
        def greet(self):
            super().greet()  # Call the greet method from Parent
            print("Hello from Child.")

Multiple Inheritance
    class Child(Mother, Father):
    
Method Resolution Order (MRO)
    D.mro()

'''