class myclass:
    

    def __init__(self):
        print("inside const")  #default too

    def __init__(self):
        pass         #default constructor


ob1 = myclass()
# In Python, you cannot overload constructors like in C++.
# the second __init__ completely replaces the first one.
# Python reads the class top to bottom, so after parsing:
#jeta pore dibi oitay execute hovbe