x = "BIKRAM SARKAR"
print(x[0])
print(x[0:6]) #its called slicing
print(x[7:13])

print(x[:]) #if no value is provided starting value is taken as 0 and endinng with n
print(len(x)) #to get the size of string

print(x.lower())
y = "bikram sarkar"
print(x.upper())
print(y.replace("sar","kar"))

string = "Hi, how are you"
string2 = "i,am,good"
list1 = string.split(" ")
list2 = string2.split(",")
print(list1)
print(list2)

file = "file.csv"
if(file.endswith(".csv")):
    print("CSV file")

if(file.startswith("fi")):
    print("fwahhhhhhhh")

if(isinstance(file,str)):
    print("yeahhhhhhhhhh")

if(file.isnumeric()==False):
    print("noooooooo")

string = "Oh tunir ma tomar tuni kotha sune na"
print(string.count("tuni"))

x = "10"  #wont work with x = 10 as the functions only works with string
if(x.isnumeric()):
    print("true")

x = 10
if(x.is_integer()):
    print("this is for integer")