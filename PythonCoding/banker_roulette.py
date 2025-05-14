import random

names = "Ojas, Ojal, Varsha, Sharvari"
name_list = names.split(",")

print(f"Today {name_list[random.randint(0, len(name_list)-1)].strip()} is going to pay the bill!")