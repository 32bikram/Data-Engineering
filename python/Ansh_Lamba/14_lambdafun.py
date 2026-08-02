def add(x, y):
    return x+y

print(add(2,3))

# does the same work as above function
add = lambda x,y: x+y
print(add(6,8))

# how is add getting overridden?
# ->
# Because in Python, functions are just variables pointing to objects.
# def add(a, b):
#     return a + b
# Python creates a function in memory and stores its reference inside add.
# add is a function object living in memory.
print(add)
def add(p,q):
    print (6+7)

print(add)