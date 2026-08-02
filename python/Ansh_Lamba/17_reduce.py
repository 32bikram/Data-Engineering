from functools import reduce

def mul(x, y):
    return (x*y)

res = reduce(mul,[1,3,4,5,2,2,1])
print (res)