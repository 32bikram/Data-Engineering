class klass:
    name = "bikram"
    roll = 3024

    def fun(self):
        print(f"my name is {self.name} my roll is {self.roll}")
    
    def fun2(self, name, roll):
        print(f"my name is {name} my roll is {roll}")

ob1 = klass()
ob1.fun()
ob1.fun2("malay", 123) #internally -> klass.fun2(ob1, "malay", 123)   thats why self is requied in function parameter
print(ob1.name)