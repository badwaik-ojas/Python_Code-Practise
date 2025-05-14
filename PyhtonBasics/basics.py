import sys
print(sys.version) 
print(sys.winver) 
print(sys.gettrace) 
print(sys.argv)

print(10%3) # provides reminder
print(9//4) # provides closest divisible value

# String Index
message = 'Hello World!'
print(message[0])
print(message[-1]) # printing from last
print("reversed: ", message[::-1])

# Length
print(len(message)) # length of string

# Slicing
print("Slicing: ",message[0:5])

# Striding in a string
print(message[::2])

# Concat
print(message + " " +message)

# Upper, Lower, Title
print("upper: "+message.upper())
print("lower: "+message.lower())
print("title: "+message.title())

# Replace
print("replace: "+message.replace('Hello','Hi'))

# Find
print("find: ",message.find("Wo"))

# eval: This function serves the aim of converting a string to an integer or a float

exp = '3+5+(4*5)'
total = eval(exp)
print(total)