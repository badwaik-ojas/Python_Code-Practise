import json

friends = {"name": "Alice", "age": 25, "pets": ["dog", "cat"]}

with open("friends.json", "w") as f:
    json.dump(friends, f, indent=4)  # Save JSON to file with pretty print

#####

import json

with open("friends.json", "r") as f:
    obj = json.load(f)

print(type(obj))   # <class 'dict'>
print(obj)         # Dictionary contents from the JSON file

#####