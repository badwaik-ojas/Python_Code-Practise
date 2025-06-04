import pickle

data = {"name": "Alice", "age": 30}

with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

with open("data.pkl", "rb") as f:
    loaded_data = pickle.load(f)

print(loaded_data)  # {'name': 'Alice', 'age': 30}

bytes_obj = pickle.dumps(data)

data_again = pickle.loads(bytes_obj)
