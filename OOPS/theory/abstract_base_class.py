from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        return "generic sound"
    
class Dog(Animal):
    def speak(self):
        return 'woooof'
    def color():
        return 'black'
    
class Cat(Animal):
    def speak(self):
        return 'meooow'

dog = Dog()
