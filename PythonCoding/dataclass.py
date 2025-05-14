'''
In Python, a dataclass is a decorator and a type hinting tool that automatically generates 
special methods like __init__(), __repr__(), __eq__(), and others for user-defined classes. 
It simplifies the creation of classes used to store data without having to write boilerplate 
code.
'''
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    # You can define methods in a dataclass like any other
    def bookinfo(self):
        return f"{self.title}, by {self.author}"


# create some instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

# access fields
print(b1.title)
print(b2.author)

# print the book itself - dataclasses provide a default
# implementation of the __repr__ function
print(b1)

# comparing two dataclasses
b3 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
print(b1 == b3)

# change some fields, call a regular class method
b1.title = "Anna Karenina"
b1.pages = 864
print(b1.bookinfo())

'''
Automatic Method Generation:
__init__(): Automatically generated to initialize instance variables.
__repr__(): Provides a readable string representation of the object.
__eq__(): Allows comparison between instances.
__lt__(), __le__(), __gt__(), __ge__(): Comparison methods can be generated if needed by using 
    the order=True parameter in the dataclass decorator.

Default Values:
You can specify default values for fields.
@dataclass
class Person:
    name: str
    age: int = 0
    city: str = "Unknown"

Immutable Dataclasses:
By setting frozen=True in the decorator, you can make the instances of the dataclass immutable.
@dataclass(frozen=True)
class Person:
    name: str
    age: int
    city: str



'''