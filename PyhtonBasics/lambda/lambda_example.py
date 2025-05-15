addition = lambda a,b: a+b
print(addition(2,4))

#### MAP

def squares(x):
    return x*x

lst = [1,2,3,4]
print(list(map(squares, lst)))

#Using lambda
print(list(map(lambda x: x*x, lst)))

### FILTER

def iseven(x):
    return x%2==0

lst = [1,2,3,4,5,6,7,7,8,8]

print(list(filter(iseven, lst)))

#using lambda
print(list(filter(lambda x: x%2==0, lst)))

