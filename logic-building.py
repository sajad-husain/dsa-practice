# How to solve any problem?
# Understand the problem: Read and Understand the statement.
# Generate Examples: create additional input output case for each problem.
# Draw Observations: Draw observations and patterns based on the examples you created.
# Start with Basic: First, think of the basic way to solve a problem 

#Check even or odd 
number = int(input("Enter a Number: "))

def findEvenOdd():
    if(number % 2 == 0):
        return True
    else:
        return False

result = findEvenOdd()
print(result)