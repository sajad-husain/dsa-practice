# import array
# import array as Arr1 # Alias for array 
from array import * #perfect we'll be using module directly 

val = array('i', [1,2,4,5,6])
print(val) #print whole array

# iterate on each element use for loop
for i in range(0, 5):
    print("simple loop",val[i], end=" ") #endl for adding spaces
    
print('\n')
# enhcaned for loop
for x in val:
    print("enhanced loop",x)
