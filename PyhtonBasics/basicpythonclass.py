class Person:
    def __init__(self, name, age):
        """
        Initialize the Person object with a name and age.
        """
        self.name = name
        self.age = age

    def display_info(self):
        """
        Display the information of the person.
        """
        print(f"Name: {self.name}, Age: {self.age}")

    def celebrate_birthday(self):
        """
        Increment the person's age by 1 and print a birthday message.
        """
        self.age += 1
        print(f"Happy Birthday {self.name}! You are now {self.age} years old.")

# Creating objects of the Person class
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Using methods of the Person class
person1.display_info()  # Output: Name: Alice, Age: 30
person2.display_info()  # Output: Name: Bob, Age: 25

# Celebrating birthdays
person1.celebrate_birthday()  # Output: Happy Birthday Alice! You are now 31 years old.
person2.celebrate_birthday()  # Output: Happy Birthday Bob! You are now 26 years old.

# Displaying information again to see updated ages
person1.display_info()  # Output: Name: Alice, Age: 31
person2.display_info()  # Output: Name: Bob, Age: 26
