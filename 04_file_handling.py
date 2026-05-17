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
    
# WRITING FILES IN PYTHON
with open("output.txt", "w") as file:
    file.write("Hell0 there!\n")
    
# Append to file
with open("output.txt", "a") as file:
    file.write("this is new text")

# write multiple files
new_lines = ["line 1", "line 2", "line 3"]
with open("output.txt", "w") as file:
    file.writelines(f"{new_lines}\n")