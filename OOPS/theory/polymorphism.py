class Animal():
    def speak(self):
        return "generic sound"
    
class Dog(Animal):
    def speak(self):
        return 'woooof'
    
class Cat(Animal):
    def speak(self):
        return 'meooow'
    
dog = Dog()
cat = Cat()
print(dog.speak())
print(cat.speak())
print("=== === === ===")

def animal_speak(animal):
    return animal.speak()

print(animal_speak(dog))
print(animal_speak(cat))

