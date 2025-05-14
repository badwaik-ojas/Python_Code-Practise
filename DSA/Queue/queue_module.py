import queue as q

# Create a custom FIFO queue with a maximum size of 3
custom_queue = q.Queue(maxsize=3)

# Check and print the initial size of the queue
print("Queue size:", custom_queue.qsize())  # Output: 0

# Add elements to the queue using the put() method
custom_queue.put(1)
custom_queue.put(2)
custom_queue.put(3)
print("Queue size after adding 3 elements:", custom_queue.qsize())  # Output: 3

# Check if the queue is full
print("Is the queue full?", custom_queue.full())  # Output: True

# Check if the queue is empty
print("Is the queue empty?", custom_queue.empty())  # Output: False

# Dequeue elements using the get() method
first_element = custom_queue.get()
print("Dequeued element:", first_element)  # Output: 1

# Print the queue size after dequeueing
print("Queue size after dequeue:", custom_queue.qsize())  # Output: 2

###                                     LIFO                        ###

import queue

# Create a LIFO queue with a maximum size of 3
lifo_queue = queue.LifoQueue(maxsize=3)

# Add elements to the LIFO queue using the put() method
lifo_queue.put(1)
lifo_queue.put(2)
lifo_queue.put(3)

# Print the queue size after inserting 3 elements
print("LIFO Queue size after adding 3 elements:", lifo_queue.qsize())  # Output: 3

# Dequeue elements using the get() method (Last In, First Out)
first_element = lifo_queue.get()
print("Dequeued element from LIFO queue:", first_element)  # Output: 3

# Print the queue size after dequeuing
print("LIFO Queue size after dequeue:", lifo_queue.qsize())  # Output: 2

# Dequeue remaining elements
print("Dequeued element from LIFO queue:", lifo_queue.get())  # Output: 2
print("Dequeued element from LIFO queue:", lifo_queue.get())  # Output: 1

###                           Priority Queue                      ###

import queue

# Create a priority queue with a maximum size of 3
priority_queue = queue.PriorityQueue(maxsize=3)

# Add elements to the priority queue (lower numbers have higher priority)
priority_queue.put((3, 'task 1'))  # Priority 3
priority_queue.put((1, 'task 2'))  # Priority 1
priority_queue.put((2, 'task 3'))  # Priority 2

# Print the queue size after inserting 3 elements
print("Priority Queue size after adding 3 elements:", priority_queue.qsize())  # Output: 3

# Dequeue elements using the get() method (Priority Order)
first_task = priority_queue.get()
print("Dequeued task from Priority queue:", first_task)  # Output: (1, 'task 2')

# Print the queue size after dequeuing
print("Priority Queue size after dequeue:", priority_queue.qsize())  # Output: 2

# Dequeue remaining tasks
print("Dequeued task from Priority queue:", priority_queue.get())  # Output: (2, 'task 3')
print("Dequeued task from Priority queue:", priority_queue.get())  # Output: (3, 'task 1')
