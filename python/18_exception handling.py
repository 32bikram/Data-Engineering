x = "90"
try:
    if(x<100):
        print("smaller")
    else:
        print("larger")

except Exception as e:
    print(e)

finally:
    print("this runs every time")

print ("hellow world")