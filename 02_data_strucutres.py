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
# number_list = [3,1,4,1,5,1,9,2,6]

# number_list.append(121) # adding at last of the list
# print("list after appending", number_list)

# number_list.extend([11,12]) # add multiple items
# print("list after extending", number_list)

# number_list.insert(0,100) # adding hundred at 0th index
# print("list after inserting", number_list)

# number_list.remove(1) # remove at 0 index
# print("list after removing the item",number_list)

# last = number_list.pop() # remove and return last value of the list 
# print(last)
# print("Popping last value", number_list)

# second = number_list.pop(1) # remove the value at index 1
# print(second)
# print("Popping value at the index", number_list)

# counted_value = number_list.count(1) # how much time 1 is appeared
# print(f"this value appeared {counted_value} times")

# index_8 = number_list.index(1) # on which index 1 exists
# print(f"on {index_8} index value appears first")

# number_list.sort()
# print(f"Sorted List {number_list}")

# number_list.reverse()
# print(f"reversed list {number_list}")


# Lambda chota function hota h jo 1 line pe likha jata h iska return type ni hota 
# def add(a,b):
#     return a + b

# lambda argument: expression
# add = lambda a , b: a + b
# print(add(5,3))

# num_list = [1,2,3,4,5,6]
# square = list(map(lambda x: x*x, num_list))
# print("Mapping and Squaring: ", square)

# filter = list(filter(lambda x: x % 2 == 0, num_list ))
# print("Filtered list ", filter)

# student = [
#     {"name": "Alice", "grade": 85},
#     {"name": "Ling Shao", "grade": 15},
#     {"name": "Proton", "grade": 65}
# ]

# student.sort(key=lambda x:x['grade'])
# print(student)

# LIST COMPREHENSION
# squared_list = []
# for i in range(5):
#     squared_list.append(i*i)
# print(squared_list)

# # another way but more elegant way

# sq = [x**2 for x in range(11)]
# print(sq)

# mul =[x*2 for x in range(5)]
# print(mul)

# words = ["hello", "world", "python"]
# uppercase = [w.upper() for w in words]
# print(uppercase)

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# evens = [ x for x in nums if x % 2 == 0]
# print(evens)

# greate_than_five = [ x for x in nums if x > 5]
# print(greate_than_five)

# result = [ x for x in nums if x % 2 == 0 and x > 4]
# print(result)

# TUPLES work same as array but their value can be accessed but can't be manipulated
# empty_tuple = ()

# single_Item = (1)
# print(single_Item)

# num_tuple = (1,2,3,4,5)
# mixed_tuple = (1, "ali", False, None)

# print(mixed_tuple)

# # Accessing tuple elemnets same as list
# print(mixed_tuple[1])
# print(mixed_tuple[-1]) # last value 
# print(mixed_tuple[-2]) # second last value 

# # length
# print("Length of this tuple is ", len(mixed_tuple))

# # Iterating throung tuple 
# for n in num_tuple:
#     print(n)
    
# # lambda function on tuple
# cube = tuple(map( lambda x: x**3, num_tuple))
# print(cube)

# # you can't append values to tuple or assign new value
# # num_tuple.append(6) not possible
# # num_tuple[1] = 2 not possible 

# # YOU CAN ADD ON TOUPLE TO ANOTHER ONE 
# num_tuple = num_tuple + (6,7,8) + (9,10)
# print("after adding more values to the tuple", num_tuple)

# # unpacking 
# a , b, c = (1,2,3)
# print( a, b, c)

# # tuples as dictionaries
# coordinates = {}

# coordinates[(0,0)] = "origin"
# coordinates[(1,1)] = "diagonal"
# coordinates[(5,3)] = "point"

# print(coordinates[0,0])


# chess_borad = {}
# chess_borad[("a", 1)] = "rook" 
# chess_borad[("b", 2)] = "knight"

# DICTIONARIES IN PYTHON
# empty_dictionary = {}
# empty_dictionary = dict() # Another way to write dictiornay 

# person = {
#     "name": "Ali",
#     "age": 25,
#     "city": "Isd"
# }
# print(person) 

# user = dict(name = "Jabir", email = "jabir@gmail.com")
# print(user)

# # mixed data dictionary 
# data = {
#     "name": "Junaid",
#     "scores": [85, 90, 78],
#     "is_active": True,
#     "salary": 50000
# }
# print(data)

# # adding more data to dictionary 
# person = {
#     "name": "Ali",
#     "age": 25,
#     "city": "Isd",
#     "hobbies": ['reading', 'coding', 'hiking']
# }
# print("after adding data to dictionary", person)

# # Accessing dictionary by key
# print(person["name"])
# print(person["age"])
# print(person["city"])
# print(person["hobbies"])

# # using get method for safe access
# print(person.get("name"))
# print(person.get("job"))
# print(person.get("job", "not there")) # default value second paramter men hogi
# print(person.get("age"))
# print(person.get("city"))
# print(person.get("hobbies"))

# if "name" in person:
#     print("key exists")
    
# person["city"] = "Moscow"
# print(person)

# # updating multiple values
# person.update({"age": 23, "job": "Developer"})
# print(person)

# # deleting values
# del person["job"]
# print("Dictionary after deleting a value", person)

inventory = {
    "apple": 50, 
    "banana": 30, 
    "orange": 20,
    "grapes": 25
}

# iterating over items
for fruits, quantity in inventory.items():
    print(f"{fruits} : {quantity}")

# get all keys
fruits = list(inventory.keys())
print(fruits)

# get all values
all_values = list(inventory.values())
print(all_values)

