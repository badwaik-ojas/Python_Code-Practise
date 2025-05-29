'''
✅ Problem Statement: Return All Codes
Given:
A string of digits, e.g. "123".

Each digit or pair of digits maps to a letter:

'1' → 'a', '2' → 'b', ..., '26' → 'z'.

Task:
Return all possible decoded strings (codes) from the input number string.

For example:

python
Copy
Edit
Input: "123"
Output: ['abc', 'aw', 'lc']
'''

def get_codes(val):
    if val <1 or val>26:
        return ''
    return chr(96+val)

def return_all_codes(s):
    if len(s)==0:
        return [""]
    if len(s)==1:
        return [get_codes(int(s))]
    output = []

    first_digit = s[0]
    if 1 <= int(first_digit) <=9:
        char1 = get_codes(int(first_digit))
        for code in return_all_codes(s[1:]):
            output.append(char1 + code)


    first_two_digits = s[:2]
    if 10 <= int(first_two_digits) <= 26:
        char2 = get_codes(int(first_two_digits))
        for code in return_all_codes(s[2:]):
            output.append(char2 + code)

    return output

s = '123'
print(return_all_codes(s))

    
