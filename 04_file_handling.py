# Open and read entire file
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

# Read line by line
with open("data.txt", "r") as file: 
    for line in file:
        print(line.strip())
    
# Read all line into list
with open("data.txt", "r") as file:
    lines = file.readlines()
    print(lines)