'''
data class is a class that is specifically designed to store data and provide a concise syntax for 
creating data objects. The dataclass decorator, introduced in Python 3.7, is used to automatically 
generate special methods like __init__, __repr__, __eq__, and others for classes. 

This reduces boilerplate code and makes the code more readable and maintainable.
'''

from dataclasses import dataclass, field
from typing import List

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    friends: List[str] = field(default_factory=list)
    email: str = field(default="unknown@example.com", repr=False)

    def add_friend(self, friend_name: str):
        self.friends.append(friend_name)

# Create an instance of Person
p = Person(name="Alice", age=30)
print(p)  # Output: Person(name='Alice', age=30, friends=[])

# Add a friend
p.add_friend("Bob")
print(p)  # Output: Person(name='Alice', age=30, friends=['Bob'])

'''
Features of Data Classes:

Automatic __init__ Method: 
    - The __init__ method is automatically generated.

Automatic __repr__ Method: 
    - Provides a readable string representation of the object.

Automatic __eq__ Method: 
    - Supports equality comparison between instances.

Type Annotations:
    - Type hints are used to specify the types of the fields.

Default Values:
    - Fields can have default values.

Default Factory:
    - Allows for more complex default values using field.
'''

'''
Immutability with frozen=True
If you want your data class to be immutable (i.e., its instances cannot be modified after creation), 
you can use the frozen=True parameter.
'''