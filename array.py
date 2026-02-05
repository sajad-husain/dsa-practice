import array

val = array.array('i', [1,2,4,5,6])
print(val) #print whole array

# iterate on each element use for loop
for i in range(0, 6):
    print("simple loop",val[i], end=" ") #endl for adding spaces
    
# enhcaned for loop
for x in val:
    print("enhanced loop",x)
