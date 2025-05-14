
def merge_dicts(dict1, dict2):
    key1 = set(dict1.keys())
    key2 = set(dict2.keys())
    common_keys = key1 | key2
    print(common_keys)
    dict = {}
    for key in common_keys:
        if key in dict1:
            dict[key] = dict1[key] + dict.get(key, 0)
        if key in dict2:
            dict[key] = dict.get(key, 0) + dict2[key]

    return dict


def merge_dicts1(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = value + result.get(key, 0)

    return result



        

dict1 = {'a': 1, 'b': 2, 'c': 3}

dict2 = {'b': 3, 'c': 4, 'd': 5}
print(merge_dicts(dict1, dict2))
print(merge_dicts1(dict1, dict2))