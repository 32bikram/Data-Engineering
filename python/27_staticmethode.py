class c:
    @staticmethod   #called decortaor
    def fun(x,y):
        print(x+y)

c.fun(9,4)  # will work for this without mentioning static 
o1 = c() 
o1.fun(8,4) #but wont work for this onea

# | Method Type     | First Parameter | Object Passed Automatically? |
# | --------------- | --------------- | ---------------------------- |
# | Normal Method   | `self`          | Yes                          |
# | `@classmethod`  | `cls`           | Yes (class object)           |
# | `@staticmethod` | None            | No                           |
