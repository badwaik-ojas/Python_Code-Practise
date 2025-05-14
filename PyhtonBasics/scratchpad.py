class Person:

# The constructor method in Python is called __init__, and it is automatically called when an instance of 
# the class is created. Constructors are used to set up initial state and assign values to object attributes.

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __hash__(self):
        return hash((self.name, self.age))

p1 = Person("O",1)
p2 = Person("L",1)

d = {p1:1, p2:2}
print(d)

l = [1,2    ,2,3,4,5]
print(l)
print(l.index(3))