'''
Polymorphism in Python allows for writing flexible, reusable, and maintainable code by enabling objects 
of different classes to be treated as instances of a common superclass.

Method Overriding: Providing specific implementations in subclasses for methods defined in the superclass.

Operator Overloading: Defining custom behavior for standard operators for user-defined types.

Function and Method Polymorphism: Writing functions and methods that can operate on objects of different 
types.

By leveraging polymorphism, you can design systems that are easier to extend and modify, ultimately 
leading to more robust and versatile applications.

Types of Polymorphism:
Compile-time Polymorphism (or Static Polymorphism): This type is achieved through method overloading or 
operator overloading. Python does not support method overloading directly (like Java or C++), but it does 
support operator overloading.

Run-time Polymorphism (or Dynamic Polymorphism): This type is achieved through method overriding, where a 
subclass provides a specific implementation of a method that is already defined in its superclass.

Benefits of Polymorphism
Code Reusability: You can write more generic and reusable code.

Flexibility and Maintainability: Makes it easier to add new types or change the behavior of existing types.

Extensibility: New classes can be added with minimal changes to existing code.

'''

class Animal:
    def sound(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

class Cow(Animal):
    def sound(self):
        return "Moo"

# Create a list of animals
animals = [Dog(), Cat(), Cow()]

# Iterate through the list and call the sound method
for animal in animals:
    print(animal.sound())

