class parent():
    def __init__(self,x):
        self.parent_name = x
    
    def fun(self):
        print("habijabi")

class child(parent):
    def __init__(self,x,y):
        self.child_name = x
        self.parent_name = y   #we must assign the parent class values if we want to acess parent class variable
        #OR use this way
        parent.__init__(self,y)

    def fun2(self):
        print()

ob = child("ram", "jodu")
print(f"{ob.parent_name}, {ob.child_name}")
ob.fun()
