class cls:
    name = "vjrn"
    roll = 854

    @property  #getter
    def fun(self):
        print(f"{self.name} has a roll no {self.roll}")
    
    @fun.setter
    def fun(self, x): #setter accepts only one value beside self
        y = x[0]
        z = x[1]
        self.name = y
        self.roll = z
ob = cls()
ob.fun      #property behaves like variable not function so no '()' due to decorator @property
ob.fun = ["erhfb",344]
ob.fun      #property can be called vby objects only