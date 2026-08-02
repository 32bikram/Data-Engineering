#“*x represents arbitrary positional arguments in Python, allowing a function to accept
#  a variable number of inputs, which are stored as a tuple.”

def  fun(*x):
    #x becomes a tuple inside the function
    print(x)

fun(5,4,5,6,7,7,8,3)