'''
Abstraction involves hiding the complex implementation details and showing only the essential 
features of an object. 

In Python, abstraction can be achieved using abc (Abstract Base Class) module.

An abstract class is a class that cannot be instantiated and is intended to be subclassed. An 
abstract method is a method that is declared but contains no implementation. Subclasses of an 
abstract class are expected to implement its abstract methods.

Abstract classes can also provide some default implementations of methods. Subclasses can 
use these implementations or override them as needed.

'''

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def habitat(self):
        pass

    def description(self):
        return "This is a shape."

class Dog(Animal):
    def sound(self):
        return "Bark"

    def habitat(self):
        return "Domestic"

class Cat(Animal):
    def sound(self):
        return "Meow"

    def habitat(self):
        return "Domestic"

class Lion(Animal):
    def sound(self):
        return "Roar"

    def habitat(self):
        return "Wild"

# Attempting to instantiate Animal will raise an error
# animal = Animal()  # TypeError: Can't instantiate abstract class Animal with abstract methods habitat, sound

# Creating instances of subclasses
dog = Dog()
cat = Cat()
lion = Lion()


# Using the methods
print(f"Dog: {dog.sound()}, Habitat: {dog.habitat()}")
print(f"Cat: {cat.sound()}, Habitat: {cat.habitat()}")
print(f"Lion: {lion.sound()}, Habitat: {lion.habitat()}")
