'''
✅ Generators in Python – Explained
🔁 What are Generators?
A generator is a simpler way to create iterators.

Uses the yield keyword to return values lazily, i.e., on the fly.

Does not store all values in memory, making it memory-efficient for large datasets or streams.

🧩 Generators vs Iterators
Feature	Iterator	Generator
Creation	Uses __iter__() and __next__()	Uses a function with yield
Syntax	Requires class-based implementation	Function-based with less boilerplate
Memory Usage	May store all items	Produces values on-demand
Performance	Can be slower for large datasets	More efficient for large or infinite sequences

🧪 Example 1: Basic Generator
python
Copy
Edit
def square(n):
    for i in range(n):
        yield i * i
✅ Usage
python
Copy
Edit
for val in square(3):
    print(val)
🔍 Output
Copy
Edit
0
1
4
🧠 What Happens:
yield pauses the function and remembers the state.

On the next iteration, it resumes from where it left off.

🧪 Example 2: Manual Iteration with next()
python
Copy
Edit
a = square(3)
print(next(a))  # 0
print(next(a))  # 1
print(next(a))  # 4
print(next(a))  # Raises StopIteration
🧪 Example 3: Multiple yield Values
python
Copy
Edit
def my_generator():
    yield 1
    yield 2
    yield 3
python
Copy
Edit
for val in my_generator():
    print(val)
🔍 Output
Copy
Edit
1
2
3
📁 Practical Use Case: Reading Large Files
✅ Problem:
Reading a large file line-by-line without loading entire file into memory.

🧪 Generator Implementation:
python
Copy
Edit
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line
✅ Usage:
python
Copy
Edit
file_path = 'large_file.txt'

for line in read_large_file(file_path):
    print(line.strip())
💡 Benefit:
Efficient memory usage, especially for large files or streams.

Lines are processed one at a time.

🧠 Key Takeaways
yield turns a function into a generator.

Generators are subclasses of iterators.

They are lazy, produce values on-demand, and maintain internal state.

Best used when:

Working with large datasets

Building pipelines

Writing memory-efficient code

⚖️ Quick Comparison Recap
Aspect	Iterator	Generator
Syntax	Requires class + methods	Function with yield
Simplicity	Verbose	Concise
Memory Usage	May be high	Low (lazy evaluation)
Use Cases	Custom iteration logic	Stream processing, large files
'''

def my_generator():
    yield 1
    yield 2
    yield 3

for val in my_generator():
    print(val)
