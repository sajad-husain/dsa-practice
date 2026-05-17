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

# write dictioy to json file
import json
data = {"name": "Alice", "age": 25, "city": "NYC"}
with open("data.json", "w") as file:
    json.dump(data, file, indent=2)
    
# count lines
with open("data.txt", "r") as file:
    line_count = sum(1 for _ in file)
    print(f"Total lines: {line_count}")

# "r" - Read (default)
with open("file.txt", "r") as f:
    content = f.read()
    
# "w" - Write (creates new, overwrites existing)
with open("file.txt", "w") as f:
    f.write("New content")
    
# "a" - Append (add to end)
with open("file.txt", "a") as f:
    f.write("Appended content")
    
# "r+" - Read and write
with open("file.txt", "r+") as f:
    content = f.read()
    f.write("Added content")

# "w+" - Write and read (overwrites)
# "a+" - Append and read
# "b" suffix - Binary mode (for images, etc.)
with open("image.jpg", "rb") as f:
    binary_data = f.read()