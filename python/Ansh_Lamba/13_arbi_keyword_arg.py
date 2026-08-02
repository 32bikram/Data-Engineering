# this is example of arbitary keyword argument,
# here the argument is converted to dictionary 
def fun(**a):
    for key, value in a.items():
        print(key, ":", value)
    # for key, value in a:
    #     print(key, ":", value) # this is wront we need to use .items() to get key value both
    
    for key in a:
        print (key)

    for value in a.values():
        print(value)

    for value in a:
        print(a.get(value)) #it doesnt crash when the value doesnt exist

    for value in a:
        print(a[value]) #it crashes if the value doesnt exist

fun(name = "Bikram", age = "23")