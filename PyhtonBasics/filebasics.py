# reading file

with open('resources/filebasics.txt', 'r') as f:
    print(f.read()) # reads complete file

with open('resources/filebasics.txt', 'r') as f:
    print(f.read(20)) # read 20 char

with open('resources/filebasics.txt', 'r') as f:
    print(f.readline()) # read line

# writing a file
lines = ["Hi I am Ojas\n","I live in Pune.\n"]
with open('resources/filebasicswrite.txt', 'w') as f:
    for line in lines:
        print(line)
        f.write(line)

# appending a file
lines = ["Ojal is my GF"]
with open('resources/filebasicswrite.txt', 'a') as f:
    for line in lines:
        print(line)
        f.write(line)

