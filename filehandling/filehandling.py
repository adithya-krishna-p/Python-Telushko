f = open('mydata','r')
# print(f.readline())
# print(f.readline())

f1 = open('abc','w')
f1.write("somthing fishy")


# for data in f:
#     print(data)

for data in f:
    f1.write( data)