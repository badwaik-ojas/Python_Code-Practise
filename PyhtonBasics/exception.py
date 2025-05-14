
try:
    1/0
except ZeroDivisionError:
    print('This code gives a ZeroDivisionError.')
finally:
    print("in finally")