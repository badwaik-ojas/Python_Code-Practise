def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

print("year 38 is a leap year? ", is_leap_year(38))
print("year 40 is a leap year? ", is_leap_year(40))
print("year 300 is a leap year? ", is_leap_year(300))

###############

def longest_word(sentence: str) -> str:
    words = sentence.split()
    return max(words, key=len)

str1 = " Hi I am Ojas, I am thirty years old"

print("Longest word in the str is ", longest_word(str1))

###############

def count_words(s: str) -> int:
    return len(s.split())

print("Word count in the str is ", count_words(str1))

###############

def is_sorted(lst: list) -> bool:
    return lst == sorted(lst)

lis1 = [1,2,3]
lis2 = [1,3,2]

print("is lis1 sorted? ",is_sorted(lis1))
print("is lis2 sorted? ",is_sorted(lis2))

###############

def list_of_squares(n: int) -> list:
    return [i**2 for i in range(1, n + 1)]

print("Precise way to create list of square? ",list_of_squares(4))

###############

def common_elements(lst1: list, lst2: list) -> list:
    return list(set(lst1) & set(lst2))

print("common element in the list of square? ", common_elements(lis1, lis2))

###############

def flatten(nested_list: list) -> list:
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

lis3 = [[1,2], [3,4,5], [4,5,6]]
print("flatten the lis3? ",flatten(lis3))

###############

def second_largest(lst: list) -> int:
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[-2] if len(unique_lst) >= 2 else None
lis4 = [3,5,4,3,6,4,11,4,5,33,5,55]

print("2nd largest number from the list? ", second_largest(lis4))

##############

def merge_sorted_lists(lst1: list, lst2: list) -> list:
    return sorted(lst1 + lst2)

print("merge 2 list: ",lis1+lis2)

###############

def count_vowels(s: str) -> int:
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

print("count vowel in a string: ",count_vowels(str1))





