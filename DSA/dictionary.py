
# Searching through a dictionary
def search_dictionary(dictionary, value):
    for key in dictionary:
        if dictionary[key] == value:
            return key, dictionary[key]
    return "The value does not exist."

MyDict = {
    'name': 'Edy',
    'age': 26,
    'address': 'London'
}

result = search_dictionary(MyDict, 26)
print(result)
result = search_dictionary(MyDict, 126)
print(result)

del MyDict['age']
print(MyDict)

MyDict = {
    'name': 'Edy',
    'age': 26,
    'address': 'London'
}

removed_element = MyDict.pop('age')
print(removed_element)


MyDict = {
    'name': 'Edy',
    'age': 26,
    'address': 'London'
}
# The popitem() method removes and returns the last inserted key-value pair. 
key, value = MyDict.popitem()
print(key)

# The clear() method removes all elements from the dictionary, leaving it empty.

MyDict.clear()

import random

city_names = ["Paris", "London", "Berlin", "Madrid", "Rome"]

city_temperatures = {city: random.randint(20, 30) for city in city_names}

hot_cities = {city: temp for city, temp in city_temperatures.items() if temp > 25}


print("All City Temperatures:", city_temperatures)
print("Cities with Temperature > 25:", hot_cities)


MyDict = {
    'name': 'Edy',
    'age': 26,
    'address': 'London'
}

#print(MyDict['X'])



