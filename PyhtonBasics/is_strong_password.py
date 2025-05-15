def is_strong_password(passsword):
    if len(passsword) < 8:
        return False
    if not any(char.isdigit() for char in passsword):
        return False
    if not any(char.islower() for char in passsword):
        return False
    if not any(char in '!@#$%^&*()~`' for char in passsword):
        return False
    if not any(char.isupper() for char in passsword):
        return False
    return True

print(is_strong_password("abccefghi"))
print(is_strong_password("1234*Test"))