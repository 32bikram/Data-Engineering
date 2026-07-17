def sq(x):
    if(x*x>10):
        return x*x
    
my_list = list(map(sq,[2,5,1,8,3,5]))
print(my_list)

#to remove this none filter is used

my_list = list(filter(sq, [1,4,5,6,2,1,2]))
print(my_list)