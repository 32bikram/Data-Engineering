def square(x):
    return x*x

print(square(3))

# now what if we wanna pass a list in the square function
my_list = [1,23,4,5,6,67,6]
result = map(square,my_list)
print (result)  #returns map object
result = list(result) # convert to list
print(result)
#map() applies a function to every element of a collection.
# it performs the operation in each item