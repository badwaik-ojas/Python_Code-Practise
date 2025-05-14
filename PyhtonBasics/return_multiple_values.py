'''
To return multiple values at different times during function execution in Python, you 
typically use the yield statement, which allows you to create a generator. A generator can 
produce multiple values one at a time and maintain its state between yields, making it 
useful for cases where you want to return intermediate results progressively.
'''

def process_data(x):
    intermediate1 = x * 2
    yield intermediate1  # Return the first intermediate result
    
    intermediate2 = intermediate1 + 1
    yield intermediate2  # Return the second intermediate result
    
    final_result = intermediate2 / 3
    yield final_result  # Return the final result

# Using the generator
gen = process_data(10)
print(next(gen))  # Output: 20 (intermediate1)
print(next(gen))  # Output: 25 (intermediate2)
print(next(gen))  # Output: 8.333333333333334 (final_result)


def get_coordinates():
    latitude = 40.7128
    longitude = -74.0060
    return latitude, longitude

# Calling the function
lat, lon = get_coordinates()
print("Latitude:", lat)
print("Longitude:", lon)

def get_numbers():
    return [1, 2, 3, 4, 5]

# Calling the function
numbers = get_numbers()
print("Numbers:", numbers)

def get_person_info():
    return {
        'name': 'Alice',
        'age': 30,
        'city': 'New York'
    }

# Calling the function
info = get_person_info()
print("Name:", info['name'])
print("Age:", info['age'])
print("City:", info['city'])

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

def get_person():
    return Person('Bob', 25, 'San Francisco')

# Calling the function
person = get_person()
print("Name:", person.name)
print("Age:", person.age)
print("City:", person.city)
