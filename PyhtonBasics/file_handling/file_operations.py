with open("PyhtonBasics/file_handling/read_file.txt", "r") as file:
    content = file.read()
    print(content)

with open("PyhtonBasics/file_handling/read_file.txt", "r") as file:
    for line in file:
        print(line.strip()) 

with open("PyhtonBasics/file_handling/write_file.txt", "w") as file:
    file.write("Hello World\n")
    file.write("This is a new line\n")