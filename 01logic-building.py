# How to solve any problem?
# Understand the problem: Read and Understand the statement.
# Generate Examples: create additional input output case for each problem.
# Draw Observations: Draw observations and patterns based on the examples you created.
# Start with Basic: First, think of the basic way to solve a problem 

#Given a number n, check whether it is even or odd. Return true for even and false for odd.
number = int(input("Enter a Number: "))

def findEvenOdd():
    if(number % 2 == 0):
        return True
    else:
        return False

result = findEvenOdd()
print(result)

# Multiplication Table
for i in range(1, 11):
    print(f"{number} x {i} = {number*i}")
    
# Sum of natural numbers
sum = 0 
for i in range(1, number + 1):
    sum += number
print("Sum of natural numbers is",sum)

# Sum of squared natural Numbers
squared_sum = 0
for i in range(1, number + 1):
    squared_sum += number^2
print(squared_sum)