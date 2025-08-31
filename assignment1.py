

'''Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen. '''


num1 = float(input("\n Enter the first number: "))
num2 = float(input("\n Enter the second number: "))

# Performed calculations
addition = num1 + num2 
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 

# Displaying the results
print(f"\n Addition: {addition}\n")
print(f"Subtraction: {subtraction}\n")
print(f"Multiplication: {multiplication}\n")
print(f"Division: {division}\n")