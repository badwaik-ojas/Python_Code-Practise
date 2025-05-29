'''
Problem Statement:
Given a string s containing distinct characters, write a function to generate all possible permutations of the characters in the string.

'''

def print_permutations(s, taken_so_far=""):

    if len(s) == 0:
        print(taken_so_far)
        return

    ch = s[0]
    rest_of_string = s[1:]

    for i in range(len(taken_so_far)+1):
        new_str = taken_so_far[i:] + ch + taken_so_far[:i]
        print_permutations(rest_of_string, new_str)

print_permutations('abc')