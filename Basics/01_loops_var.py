#import magic_variables
import math

varint = 1
varfloat = 10.2
varstr = "test"
varlist = [1,2,3,4,5,6,7,8,9]
vartuple = (1,2,2,1,2)
vardict = { 'a':1, 'b':2}

print(type(varint), varint)
print(type(varfloat), varfloat)
print(type(varstr), varstr)
print(type(varlist), varlist, varlist[1])
print(type(vartuple), vartuple, "Count:", vartuple.count(2), " Index:", vartuple.index(2))
print(type(vardict), vardict['a'])

for val in varlist:
    print(val, end = " ")
print()

print("print with index values")
for index, val in enumerate(varlist):
    print("["+str(index)+"]",":", val)
print()


print("For with range")
for val in range(0,15):
    print(val,end=" ")
print()

entity="Apple"

match entity:
    case "Apple" | "Banana" | "Grapes":
        print("Fruit")
    case "Potato" | "Brinjal" | "Tomato":
        print("Vegetable")
    case _:
        print("Something else")

