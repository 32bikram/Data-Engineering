class c:
    name = "bikram"
    roll = 3768

    def __init__(self,x,y):
        self.name = x
        self.roll = y

    def res(self):
        print(f"my name is {self.name} and roll {self.roll}")

    def change(self,x,y):
        c.name = x
        c.roll = y
    #using classmethode we dont need to use the class name, only self or the keyword we pass is required    
    @classmethod
    def change(cls,x,y):     #cls can be anything(abcd,xyz), this methode is used to change the value for whole class not just the object
        cls.name = x
        cls.roll = y

ob2 = c("mai",1)
print(ob2.res()) #res isnt returning anything thats why none is getting printed

print(c.name) #ob2 changed the value only for itself not the whole class
c.name = "mama"
print(c.name)

ob2.change("fgb",84)
print(c.name,c.roll)