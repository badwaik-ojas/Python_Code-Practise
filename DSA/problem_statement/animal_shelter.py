'''
We need to design a data structure for an animal shelter that contains only cats and dogs. The shelter should operate on a First-In-First-Out (FIFO) basis, with the following operations:

Enqueue: Add a new animal to the shelter (either a dog or a cat).
DequeueAny: Adopt the oldest animal, regardless of type.
DequeueDog: Adopt the oldest dog.
DequeueCat: Adopt the oldest cat.
'''

from collections import deque
import itertools

class Animal:
    def __init__(self, name, animal_type, timestamp):
        self.name = name
        self.type = animal_type  # "cat" or "dog"
        self.timestamp = timestamp

    def __repr__(self):
        return f"{self.type.capitalize()}({self.name})"

class AnimalShelter:
    def __init__(self):
        self.dogs = deque()  # Queue for dogs
        self.cats = deque()  # Queue for cats
        self.timestamp_counter = itertools.count()  # Unique timestamps for arrival order

    def enqueue(self, name, animal_type):
        # Assign a unique timestamp to the animal
        timestamp = next(self.timestamp_counter)
        animal = Animal(name, animal_type, timestamp)
        
        if animal_type == "dog":
            self.dogs.append(animal)
        elif animal_type == "cat":
            self.cats.append(animal)
        else:
            raise ValueError("Animal type must be 'dog' or 'cat'.")

    def dequeueDog(self):
        if not self.dogs:
            return None
        return self.dogs.popleft()

    def dequeueCat(self):
        if not self.cats:
            return None
        return self.cats.popleft()

    def dequeueAny(self):
        if not self.dogs and not self.cats:
            return None  # No animals available
        
        # If either queue is empty, adopt from the non-empty queue
        if not self.dogs:
            return self.dequeueCat()
        if not self.cats:
            return self.dequeueDog()
        
        # Compare timestamps to determine the oldest animal
        if self.dogs[0].timestamp < self.cats[0].timestamp:
            return self.dequeueDog()
        else:
            return self.dequeueCat()

    def __repr__(self):
        return f"Dogs: {list(self.dogs)}, Cats: {list(self.cats)}"

shelter = AnimalShelter()

shelter.enqueue("cat1", "cat")
shelter.enqueue("dog1", "dog")
shelter.enqueue("cat2", "cat")
shelter.enqueue("dog2", "dog")
print(shelter)
# Output: Dogs: [Dog(dog1), Dog(dog2)], Cats: [Cat(cat1), Cat(cat2)]

print(shelter.dequeueCat())  # Output: Cat(cat1)

print(shelter.dequeueDog())  # Output: Dog(dog1)

print(shelter.dequeueAny())  # Output: Cat(cat2)

print(shelter)
# Output: Dogs: [Dog(dog2)], Cats: []
