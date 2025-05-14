'''
📌 1. Normal Assignment (=)
This does not create a copy. It just creates a new reference to the same object in memory.
'''
a = [1, 2, 3]
b = a          # b points to the same object as a

b[0] = 99
print(a)       # [99, 2, 3] → a is also affected
'''
📌 2. Shallow Copy (copy.copy() or slice or .copy())
Creates a new outer object, but the inner objects are still references.
'''
import copy

a = [[1, 2], [3, 4]]
b = copy.copy(a)  # or b = a[:] for lists

b[0][0] = 99
print(a)  # [[99, 2], [3, 4]] → inner objects are shared
'''
So:
✅ Outer list is copied
❌ Inner lists are not copied (shared references)

📌 3. Deep Copy (copy.deepcopy())
Creates a completely independent copy, including all nested objects.
'''
import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)

b[0][0] = 99
print(a)  # [[1, 2], [3, 4]] → completely unaffected
'''
🔍 Summary Table
Copy Type	        Outer Object    Inner Objects	Use When
=	                Shared	        Shared	        Just need a new name/reference
copy.copy()	        New	            Shared	        You need a shallow structure copy
copy.deepcopy()	    New	            New	            You need a full independent copy
'''
