#Separation
print("bikram",23,"male",sep = "%")
print('bikram',23,'male',sep = '%')
print("bikram",23,'male',sep = '%')
#in python we have the liberty to use " ' " or " "" " in print 

#how do we write in new line?
print("""you can 
use 
double quote""")
print("")
print('''you
can 
use this too''')
#will automatically go to new line as python is line by line interpreted

print('hi myself "BIKRAM SARKAR"')
print("hi myself 'BIKRAM SARKAR'")
print("hi myself \"BIKRAM SARKAR\"")
# here "\" is called escape character

x = "bikram"
y = "10" # y = 10 will throw error
print(x+y)

'''this is a comment'''
''' this too is
a comment'''

# "\" allows to erite code in multiple lines
total = 10+11+12+85+95
total2 = 10+11+\
12+85+95 #here is the use of "\"
total3 = (10+11+
12+85+95)
print(str(total)+" "+str(total2))
print(f"{total} {total2} {total3}") #f string methode

#indentation
x = 1
if(x==1):
    print("yes")
print("NOT OF IF")

#Explicit typecasting
x = 11
y = "11"
a = int(y)
b = str(x)
print(type(a),type(b))

#type casting
i = 5
j = 2 #both are int
print(i/j) #but result will be float