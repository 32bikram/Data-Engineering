x = 2001
if(x==10):
    print("x is 10")
elif(x>=10):
    print("x is bigger")
    if(x<500):
        print("less than 500")
    elif((x>1000) & (x<2000)):  #if you write elif(x>1000 & x<2000) it returns true,
                                #even though x is bigger than 2000
        print("less than 2000")
    elif(10<x<3000):
        print("yeas")
else:
    print("x isnt 10")
