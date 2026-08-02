my_tup = (91,2,3,4,5,6)
print(my_tup)
my_list = list(my_tup) #type conversion to list
my_list.append(92)
print(my_list)
my_tup = tuple(my_list) #again type conversion to tuple
print(my_tup)