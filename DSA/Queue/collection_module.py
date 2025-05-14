from collections import deque
queue = deque(maxlen=3)

queue.append(1)
queue.append(2)
queue.append(3)

removed_element = queue.popleft()

queue.clear()

queue = deque(maxlen=3)

# Print initial queue (should be empty)
print(queue)

# Enqueue elements using append
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)  # Queue after adding 1, 2, and 3

# Enqueue an additional element (this will overwrite the oldest element if the queue is full)
queue.append(4)
print(queue)  # Queue after adding 4, the oldest element (1) is removed