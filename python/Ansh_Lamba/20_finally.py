def fun():
    try:
        print("in try")
        return 1
    
    except:
        print("inside except")
    
    finally:
        print("this will run inside functiontoo even after return statement")
        return 2 #it will even override the return value by the function too
    
x = fun()
print (x) 
