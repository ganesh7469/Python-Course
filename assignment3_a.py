

''' Write a Python program that:

1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.'''


# Implementation

num = int(input("Enter a number: "))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Call the function with a sample number
result = factorial(num)
print("The factorial of", num, "is:", result)
