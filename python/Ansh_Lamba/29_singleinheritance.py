class parent():
    def fun(self):
        print("parent class")
    
    def fun2(self):
        print("calling parent class function")

class child(parent):
    def fun(self):
        super().fun()  #this calls the parent class fun
        #super is a function call that returns a special object representing the parent class.
        print("child class")

ob = child()
ob.fun() #the child class does override
ob.fun2()