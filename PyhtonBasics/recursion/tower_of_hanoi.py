'''
🏯 Tower of Hanoi (Recursion Problem)
❓ Problem Statement
You are given three towers (pegs):

Source (S)

Destination (D)

Auxiliary (A)

You also have n disks of different sizes stacked in decreasing size on the Source tower.
Your goal is to move all the disks from the Source to the Destination using the Auxiliary tower, following these rules:

📜 Rules
Only one disk can be moved at a time.

A larger disk cannot be placed on top of a smaller disk.    
'''

steps = 0
def tower_of_hanoi(n, source, destination, auxillary):
    global steps

    if n == 0:
        return
    if n == 1:
        steps +=1
        print(f"Steps {steps}: Move disk 1 from {source} to {destination}")
        return
    
    tower_of_hanoi(n-1, source, auxillary, destination)
    steps +=1
    print(f"Steps {steps}: Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n-1, auxillary, destination, source)

tower_of_hanoi(3, 'a', 'b', 'c')