myset = {1,2,3,4,4,4,4,4,5}
newset = {1,2,6,7,8,9}

print(type(myset))
print(myset) #auto remove duplicates
print(myset.union(newset))
print(myset.intersection(newset))

a = {} #dictionary
print(type(a))
a = set()
print(type(a))

myset.add(112) #position where this is added is random
print(myset)

myset.remove(4)
print(myset)