# import array
# import array as Arr1 # Alias for array 
from array import * #perfect we'll be using module directly 
# import numpy as np
from numpy import *

# val = array('i', [1,2,3,4,5,6,7,8,9])
# print(val) #print whole array

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

# print("createing a  new array and inserting previous array in it")
# copyArray = array(val.typecode, (x*3 for x in val))

# # no index will delete last element, now it's deleting 3rd index
# print("deleting last element of array", copyArray.pop(3))

# # this methods remves element whichever you provide
# copyArray.remove(6)

# print("Slicing in Arrays")
# #  newArray = val[start index jo include hoga : end index include ni hoga]
# # newArray = val[ 2 : 5 ] # 2 index se start 5th index exlude
# # newArray = val[2 : -3] # 2 index se start last k 3 index ko chor print krega sb
# newArray = val[ :: -1] # revere krega aray ko 

# for i in newArray:
#     print(i, end=" ")

# arr1 = array('i', [1,2,3,4,5,6,7])
# # n = int(input("Enter length of array: "))

# # for i in range(0, n):
# #     arr1.append(int(input("Enter next element: ")))

# searchedElement = arr1.index(4)

# print(searchedElement)

print("===NUMPY MODULE===")
# you can create array direct while using numpy module
val = array([1,2,4]) 

for i in val:
    print(i, end=" ")