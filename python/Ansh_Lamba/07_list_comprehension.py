mylist = [0,1,2,3,4,5,6]
# newlist = []
# for i in mylist:
#     newlist.append(i*i)
# print(newlist)

newlist = [i*i for i in mylist if (i%2)==0 if (i*i>10)]
print(newlist)