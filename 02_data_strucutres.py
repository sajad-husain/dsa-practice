# empty_list = []

# list_with_data = [1,2,3,4,5]

# mix_list = [1, "Junaid", True, None]

# print(f"Empty List {empty_list}, \nFilled List: {list_with_data}, \nList with mixed data: {mix_list}")

# # using list constructor
# constructor_list = list("Ali")
# print(constructor_list)
# print(list("SAJJAD")) # alternative way to write a list

# #range based lists
# ranged_list = list(range(6))
# print("Ranged list: ", ranged_list)

# # Accessing elements in lists
# fruits = ["Apple", "Oranges", "Cherry", "Banana"]
# print(fruits)

# # Indexing based
# print(fruits[2])
# print(fruits[0])
# print(fruits[-1]) # last element
# print(fruits[-2]) # second last element

# # length of list
# print("length of this list is", len(fruits) )

# # Checking if element exists in a list or not
# if "Cherry" in fruits:
#     print("Cherry Exists")
    
# # MODIFYING LISTS
# numbers = [1,2,3,4,5]

# # change an element
# numbers[0] = 10
# print(numbers)

# # Add an element
# numbers.append(6)
# print(numbers)

# # Remove an element
# numbers.remove(6)
# print(f"after removing string looks like this: {numbers}")

# # inserting at specific position
# numbers.insert(1,99) # at index 1 add 99
# print(numbers)

# # delete by using index
# del numbers[0] #deleted the value at index 0
# print("Deleted now list looks like this", numbers)

# LIST METHODS
number_list = [3,1,4,1,5,1,9,2,6]

number_list.append(121) # adding at last of the list
print("list after appending", number_list)

number_list.extend([11,12]) # add multiple items
print("list after extending", number_list)

number_list.insert(0,100) # adding hundred at 0th index
print("list after inserting", number_list)

number_list.remove(1) # remove at 0 index
print("list after removing the item",number_list)

last = number_list.pop() # remove and return last value of the list 
print(last)
print("Popping last value", number_list)

second = number_list.pop(1) # remove the value at index 1
print(second)
print("Popping value at the index", number_list)

counted_value = number_list.count(1) # how much time 1 is appeared
print(f"this value appeared {counted_value} times")

index_8 = number_list.index(1) # on which index 1 exists
print(f"on {index_8} index value appears first")

number_list.sort()
print(f"Sorted List {number_list}")

number_list.reverse()
print(f"reversed list {number_list}")

student = [
    {"name": "Alice", "grade": 85},
    {"name": "Ling Shao", "grade": 15},
    {"name": "Proton", "grade": 65}
]

