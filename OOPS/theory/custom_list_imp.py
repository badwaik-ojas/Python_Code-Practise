import ctypes

class CustomList:
    def __init__(self):
        """Initialize the custom list with initial capacity of 1"""
        self.capacity = 1  # Initial capacity - how much we can store
        self.size = 0      # Current size - how much is currently stored
        self.array = self._create_array(self.capacity)  # Create the internal array
    
    def _create_array(self, capacity):
        """Create a new array with given capacity"""
        # Create a referential array using ctypes
        return (capacity * ctypes.py_object)()
    
    def _resize(self, new_capacity):
        """Resize the array to new capacity"""
        # Create a new array with the new capacity
        new_array = self._create_array(new_capacity)
        
        # Copy all elements from old array to new array
        for i in range(self.size):
            new_array[i] = self.array[i]
        
        # Replace the old array with new array
        self.array = new_array
        # Update capacity
        self.capacity = new_capacity
    
    def append(self, item):
        """Add an item to the end of the list"""
        # Check if array is full
        if self.size == self.capacity:
            # Resize to double the capacity
            self._resize(2 * self.capacity)
        
        # Add the item at the current size index
        self.array[self.size] = item
        # Increase the size
        self.size += 1
    
    def pop(self):
        """Remove and return the last element from the list"""
        # Check if list is empty
        if self.size == 0:
            raise IndexError("pop from empty list")
        
        # Get the last item
        popped_item = self.array[self.size - 1]
        # Decrease the size
        self.size -= 1
        # Return the popped item
        return popped_item
    
    def __len__(self):
        """Return the length of the list (called by len() function)"""
        return self.size
    
    def __str__(self):
        """Return string representation of the list (called by print() function)"""
        output = ""
        
        # Build the string representation
        for i in range(self.size):
            output = output + str(self.array[i]) + ","
        
        # Remove the last comma and add square brackets
        if output:
            output = "[" + output[:-1] + "]"  # Remove last comma with slicing
        else:
            output = "[]"  # Empty list case
        
        return output
    
    def __getitem__(self, index):
        """Get item by index (called when using square brackets like my_list[0])"""
        # Check if index is valid
        if 0 <= index < self.size:
            return self.array[index]
        else:
            raise IndexError("invalid index")
    
    def clear(self):
        """Clear all elements from the list"""
        # Simply reset the size to 0
        # We don't need to actually delete anything from memory
        self.size = 0
    
    def insert(self, position, element):
        """Insert an element at the specified position"""
        # Check if we need more space
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        
        # Shift elements to the right starting from the end
        # We loop backwards to avoid overwriting data we still need
        for index in range(self.size, position, -1):
            self.array[index] = self.array[index - 1]
        
        # Insert the new element at the specified position
        self.array[position] = element
        # Increase the size
        self.size += 1
    
    def remove(self, element):
        """Remove the first occurrence of the specified element"""
        # Step 1: Find the element
        for i in range(self.size):
            if self.array[i] == element:
                # Step 2: Shift everything to the left
                for j in range(i, self.size - 1):
                    self.array[j] = self.array[j + 1]
                # Step 3: Decrease size
                self.size -= 1
                return  # Stop after removing first occurrence
        
        # If we get here, element wasn't found
        raise ValueError(f"list.remove(x): x not in list")


# Example usage and testing
if __name__ == "__main__":
    # Create a custom list
    my_list = CustomList()
    
    # Test basic operations
    print("=== Testing Basic Operations ===")
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    my_list.append(4)
    print("After adding 1,2,3,4:", my_list)
    print("Length:", len(my_list))
    
    # Test indexing
    print("\n=== Testing Indexing ===")
    print("my_list[0]:", my_list[0])
    print("my_list[2]:", my_list[2])
    
    # Test insert
    print("\n=== Testing Insert ===")
    print("Before insert:", my_list)
    my_list.insert(1, 100)  # Insert 100 at position 1
    print("After inserting 100 at position 1:", my_list)
    
    my_list.insert(0, 50)   # Insert 50 at the beginning
    print("After inserting 50 at position 0:", my_list)
    
    # Test remove
    print("\n=== Testing Remove ===")
    print("Before remove:", my_list)
    my_list.remove(100)     # Remove first occurrence of 100
    print("After removing 100:", my_list)
    
    # Test clear
    print("\n=== Testing Clear ===")
    print("Before clear:", my_list)
    my_list.clear()
    print("After clear:", my_list)
    print("Length after clear:", len(my_list))
    
    # Test error cases
    print("\n=== Testing Error Cases ===")
    try:
        print(my_list[0])  # Should raise IndexError
    except IndexError as e:
        print("IndexError caught:", e)
    
    try:
        my_list.pop()  # Should raise IndexError
    except IndexError as e:
        print("Pop error caught:", e)
    
    try:
        my_list.remove(999)  # Should raise ValueError
    except ValueError as e:
        print("Remove error caught:", e)
    
    # Test with mixed data types
    print("\n=== Testing Mixed Data Types ===")
    mixed_list = CustomList()
    mixed_list.append("hello")
    mixed_list.append(42)
    mixed_list.append([1, 2, 3])
    mixed_list.append({"key": "value"})
    print("Mixed list:", mixed_list)
    
    # Test multiple inserts and removes
    print("\n=== Testing Complex Operations ===")
    test_list = CustomList()
    for i in range(5):
        test_list.append(i * 10)
    print("Initial list:", test_list)
    
    test_list.insert(2, 99)
    print("After insert(2, 99):", test_list)
    
    test_list.remove(20)
    print("After remove(20):", test_list)
    
    print("Final length:", len(test_list))