'''
Handling null values (referred to as None in Python) is a common requirement in many programming tasks. 
Python provides several ways to handle and check for None values effectively. 
'''

value = None

# Using if Statements:
if value is None:
    print("Value is None")
else:
    print("Value is not None")

# Providing Default Values:
result = value or "default value"
print(result)

# Dictionary get Method:
data = {"name": "Alice"}
name = data.get("name", "Unknown")
print(name)

# try and except Blocks:
def process_value(value):
    try:
        result = value.upper()  # This will fail if value is None
    except AttributeError:
        result = "default value"
    return result

value = None
print(process_value(value))  # Output: default value
