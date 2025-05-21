import os 


new_dir = 'D:/Python/TestCode/PyhtonBasics/file_handling/new_dir_test'
if os.path.exists(new_dir):
    print(f"The path '{new_dir}' exists")
else:
    os.makedirs(new_dir)
    print("directory created")
    print(f"The path '{new_dir}' did not exist")


# list files
os.listdir(".")