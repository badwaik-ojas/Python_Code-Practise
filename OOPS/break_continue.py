'''
break:
The break statement is used to exit the current loop prematurely, 
regardless of the loop's condition. It can be used in for and while loops.

'''

for i in range(10):
    if i == 5:
        break
    print(i)

'''
continue
The continue statement skips the rest of the code inside the current 
iteration of the loop and moves to the next iteration.
'''

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)


