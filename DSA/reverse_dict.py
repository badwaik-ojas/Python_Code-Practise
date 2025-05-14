def reverse_dict(my_dict):
    # TODO
    result = {}
    for key, value in my_dict.items():
        result[value]= key
        
    return result

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(reverse_dict(my_dict))

def reverse_dict1(my_dict):        
    return {v:k for k, v in my_dict.items()}
print(reverse_dict1(my_dict))

