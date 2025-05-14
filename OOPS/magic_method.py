'''
In Python, magic methods (also known as dunder methods because they have double underscores before and 
after their names) allow you to define the behavior of objects for built-in operations and functions. 

They enable you to create custom behavior for various operations such as arithmetic operations, comparisons, 
attribute access, iteration, and more.
'''

class Person:

# The constructor method in Python is called __init__, and it is automatically called when an instance of 
# the class is created. Constructors are used to set up initial state and assign values to object attributes.

    def __init__(self, name, age):
        self.name = name
        self.age = age

# The __eq__ method in Python is a special method used to define the behavior of the equality 
# operator == for instances of a class. By default, the == operator checks for object identity 
# (whether two variables refer to the same object). 
    
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False
    
# The __hash__ method in Python is used to define the hash value of an object, which is an integer used
# to quickly compare dictionary keys during a dictionary lookup. Objects that are used as dictionary keys
# must have a __hash__ method, and they must also be immutable, or at least appear immutable to the hash
# table, so that the hash value remains constant.

# __hash__ Method: The __hash__ method returns the hash of a tuple containing the name and age attributes. 
# This ensures that the hash value is based on the same attributes used in the __eq__ method.

# Instances of Person can be used as dictionary keys because they implement __hash__. The dictionary 
# lookup for person2 works correctly because person1 and person2 are considered equal and have the same 
# hash value.

# The __hash__ method in Python is crucial for objects that are intended to be used as keys in hash-based
# collections like dictionaries and sets. When overriding __eq__, it's important to also override __hash__
# to maintain the consistency of equality and hash values. For mutable objects, ensure that the attributes
# used in __eq__ and __hash__ are immutable to avoid inconsistencies. 

    def __hash__(self):
        print(hash((self.name, self.age)))
        return hash((self.name, self.age))
    
    def __str__(self):
        return f"({self.name}, {self.age})"

# Creating instances of the Person class
person1 = Person("Alice", 30)
person2 = Person("Alice", 30)
person3 = Person("Bob", 25)
print(person3)
# Using instances as dictionary keys
people_dict = {person1: "Person 1", person3: "Person 3"}

# Checking for equality and dictionary lookup
# print(person1 == person2)  # Output: True
# print(person1 == person3)  # Output: False
print(people_dict[person2])  # Output: Person 1
