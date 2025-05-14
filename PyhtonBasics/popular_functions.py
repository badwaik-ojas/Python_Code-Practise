# filter

lis = [1,2,3,4,5,6,7,8]
y = filter(lambda x: x%2!=0, lis)
print(list(y))

# map
z = map(lambda x: x**2, lis)
print(list(z))

# isalnum(): It returns True if all characters in the string are alphanumeric.
text = 'Hello, Python!'
print(text.isalnum())

# isalpha(): It returns True if all characters in the string are alphabets.
# White spaces are not considered as alphabets and thus it returns False
text = 'Hello'
print(text.isalpha())

# isdecimal(): It returns True if all the characters in the given string are decimal numbers ( 0-9).
text = '3777'
print(text.isdecimal())

# isdigit(): This function returns True if all the characters in the string and the Unicode characters are digits.
numbered_text = '011235813'
print(numbered_text.isdigit())

# isspace(): It returns True if all the characters in the string are whitespaces.
space = ' '
print(space.isspace())

# The function islower() returns True if all the characters in the string are lower case, on the contrary False.
text = 'Hello, Python!'
print(text.islower())

# The function lower() converts the certain string to lower case.
print(text.lower())

# The function isupper() returns True if all the characters in the string are upper case, on the contrary False.
text = 'Hello, Python!'
print(text.isupper())

# The function upper() converts the string to uppercase.
print(text.upper())

# strip(): removes spaces from right and left
# lstrip(): removes spaces from left
# rstrip(): removes spaces from right

# replace(): Replaces a specified phrase with another specified phrase

# partition(): It searches for a specified string, and splits the string into a tuple containing three elements
    # The first element contains the part before the specified string.
    # likewise other.

# title(): This function converts the first character in the given string into uppercase
print(text.replace("l","L"))
l = text.partition(" ")
print(l)

lis1 = ["Hi", "I", "am", "Ojas"]

print(" ".join(lis1))

