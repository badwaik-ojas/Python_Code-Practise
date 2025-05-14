def max_value_key(my_dict):
    temp = 0
    index = 0
    for key, value in my_dict.items():
        if value > temp:
            temp = value
            index = key
    return index

def max_value_key1(my_dict):
    return max(my_dict, key=my_dict.get)


my_dict = {'a': 5, 'b': 9, 'c': 2}
print(max_value_key(my_dict))
print(max_value_key1(my_dict))