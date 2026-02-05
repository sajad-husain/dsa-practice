# import array
# import array as Arr1 # Alias for array 
from array import * #perfect we'll be using module directly 

val = array('i', [1,2,4,5,6])
print(val) #print whole array

# # iterate on each element use for loop
# for i in range(0, 5):
#     print("simple loop",val[i], end=" ") #endl for adding spaces

# print('\n')
# # taking simple array to next level
# for i in range(0, len(val)):
#     print(val[i])

# print('\n')
# # enhcaned for loop if array size changes than simple loop wont be efficent
# for x in val:
#     print("enhanced loop",x)

# print('\n')
# print("checking type code", val.typecode)

# print("reversing the array")
# val.reverse()

# print("inserting an element in array", val.insert(1, 90))
# print("adding elemet in end", val.append(121))

print("createing a  new array and inserting previous array in it")
copyArray = array(val.typecode, (x*3 for x in val))

for i in copyArray:
    print(i, end=" ")

