from array import array

arr = array('i',[1])
print(arr)

# Create an array
my_array = array('i', [1, 2, 3, 4])

# Insert an element at the beginning
my_array.insert(0, 6)  # Insert 6 at index 0
print(my_array)  # Output: array('i', [6, 1, 2, 3, 4])

# Insert an element in the middle (at index 2)
my_array.insert(2, 6)  # Insert 6 at index 2
print(my_array)  # Output: array('i', [6, 1, 6, 2, 3, 4])

# Insert an element at the end
my_array.insert(len(my_array), 6)  # Insert 6 at the end
print(my_array)  # Output: array('i', [6, 1, 6, 2, 3, 4, 6])

#######

def accessElement(arr, index):
    # Check if the index is out of bounds
    if index >= len(arr) or index < 0:
        return "Index out of range"
    else:
        return arr[index]  # Access and return the element at the given index

arr1 = [1, 2, 3, 4, 5, 6]

# Access valid index
print(accessElement(arr1, 1))  # Output: 2

# Access invalid index
print(accessElement(arr1, 8))  # Output: Index out of range

# Access the last valid index
print(accessElement(arr1, 5))  # Output: 6
arr1 = [1, 2, 3, 4, 5, 6]

# Access valid index
print(accessElement(arr1, 1))  # Output: 2

# Access invalid index
print(accessElement(arr1, 8))  # Output: Index out of range

# Access the last valid index
print(accessElement(arr1, 5))  # Output: 6

##### Searching

def linearSearch(arr, target):
    # Iterate through the array
    for i in range(len(arr)):
        if arr[i] == target:  # If target is found
            return i          # Return the index
    return -1                 # Return -1 if target is not found

arr = [1, 2, 3, 4, 5]
print(linearSearch(arr, 5))  # Output: 4 (since 5 is at index 4)
print(linearSearch(arr, 8))  # Output: -1 (since 8 is not in the array)

############

def deleteElement(arr, value):
    try:
        # Find the index of the value to delete
        index = arr.index(value)
        # Shift elements to the left
        for i in range(index, len(arr) - 1):
            arr[i] = arr[i + 1]
        # Remove the last element (duplicate)
        arr.pop()  # This reduces the size of the array
    except ValueError:
        print("Element not found in the array.")

# Example usage:
arr = [1, 2, 3, 4, 5, 2, 6]
deleteElement(arr, 2)
print(arr)  # Output: [1, 3, 4, 5, 6]

######

my_array = array('i', [1, 2, 3, 4, 5])

# append:
my_array.append(6)
print(my_array)

# Inserting
my_array.insert(0, 11)  # Inserts 11 at the beginning
print(my_array)

# Extending and array
my_array2 = array('i', [10, 11, 12])
my_array.extend(my_array2)
print(my_array)

# Inserting list
tempList = [20, 21, 22]
my_array.fromlist(tempList)
print(my_array)

# Removing an element at nth position: O(n)
my_array.remove(11)  # Removes the first occurrence of 11
print(my_array)

# Removing last element
my_array.pop()  # Removes the last element
print(my_array)

# Finding index of element
index_of_21 = my_array.index(21)
print(index_of_21)  # Output: Index of 21

# Reversing
my_array.reverse()
print(my_array)

# Counting element occurance
count_of_11 = my_array.count(11)
print(count_of_11)

# Covert array to string
#strTemp = ' '.join(my_array)
#print(strTemp)  # Displays a string representation

# tp list
my_list = my_array.tolist()
print(my_list)

# Slicing
sliced_array = my_array[1:4]  # Slices from index 1 to 3 (4 is not included)
print(sliced_array)

#################################

import numpy as np

# Existing two-dimensional array
array = np.array([
    [11, 12, 13],
    [14, 15, 16],
    [17, 18, 19]
])

# Adding a new column
new_column = np.array([[10], [20], [30]])
new_array = np.insert(array, [0], new_column, axis=1)  # axis=1 for column
print("Array after inserting new column:")
print(new_array)
new_array = np.insert(array, 0, new_column, axis=1)  # axis=1 for column
print("Array after inserting new column:")
print(new_array)

# Adding a new row
new_row = np.array([[5, 6, 7]])
new_array_row = np.insert(array, 0, new_row, axis=0)  # axis=0 for row
print("Array after inserting new row:")
print(new_array_row)

#########

# Sample two-dimensional array
array = np.array([
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
    [26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35]
])

# Function to access an element in a two-dimensional array
def access_element(array, row_index, column_index):
    # Check if the indices are within the bounds of the array
    if row_index >= len(array) or column_index >= len(array[0]):
        print("Incorrect index")
        return
    # Access the element
    print("Element at ({}, {}): {}".format(row_index, column_index, array[row_index][column_index]))

# Test the function
access_element(array, 1, 2)  # Should return 18
access_element(array, 2, 3)  # Should return 24
access_element(array, 10, 3)

#############

import numpy as np

# Creating a sample two-dimensional array
array = np.array([
    [11, 15, 10],
    [10, 14, 11],
    [12, 17, 12]
])

# Deleting the first row
new_array_row_deleted = np.delete(array, 0, axis=0)
print("Array after deleting the first row:")
print(new_array_row_deleted)

# Deleting the first column
new_array_column_deleted = np.delete(array, 0, axis=1)
print("\nArray after deleting the first column:")
print(new_array_column_deleted)






