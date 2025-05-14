
def check_same_frequency(list1, list2):
    # TODO
    dict1 = {}
    dict2 = {}
    for i, element in enumerate(list1):
        dict1[element] = dict1.get(element, 0) + 1
    for i, element in enumerate(list2):
        dict2[element] = dict2.get(element, 0) + 1
        
    return dict2 == dict1
       
    
list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
print(check_same_frequency(list1, list2))