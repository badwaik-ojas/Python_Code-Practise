import re

# Email validation function
def is_valid_email(email):
    """This function checks if the email is valid."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+$'
    return re.match(pattern, email) is not None

# Calling the function
print(is_valid_email("test@example.com"))  # Output: True
print(is_valid_email("invalid-email"))  # Output: False
