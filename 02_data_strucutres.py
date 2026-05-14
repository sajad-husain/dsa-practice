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
    
# MODIFYING LISTS
numbers = [1,2,3,4,5]

# change an element
numbers[0] = 10
print(numbers)

# Add an element
numbers.append(6)
print(numbers)

# Remove an element
numbers.remove(6)
print(f"after removing string looks like this: {numbers}")

# inserting at specific position
numbers.insert(1,99) # at index 1 add 99
print(numbers)

# delete by using index
del numbers[0] #deleted the value at index 0
print("Deleted now list looks like this", numbers)