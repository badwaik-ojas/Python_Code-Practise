'''
Problem Statement:
You are given a string s. Your task is to generate all possible subsequences of the string.

A subsequence is a sequence that can be derived from another string by deleting zero or more characters without changing the order of the remaining character
'''

def sub_sequence(st):
    result = []
    def helper(index, current):
        if index == len(st):
            result.insert(0, current)
            return

        helper(index + 1, current + st[index])

        helper(index + 1, current)
    helper(0, "")
    return result

st = 'abc'
print(sub_sequence(st))

