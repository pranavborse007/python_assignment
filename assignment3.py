# ASSIGNMENT 3:
# Module 4: Functions & Modules in Python 
# Task 1: Calculate Factorial Using a Function 
# 1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
# 2.   Returns the calculated factorial.
# 3.   Calls the function with a sample number and prints the output.


# Function to calculate factorial
def factorial(n):
    result = 1
    # Using a loop
    for i in range(1, n + 1):
        result *= i
    return result

# Call the function with a sample number
num = int(input("enter a number : "))
print("Factorial of", num, "is:", factorial(num))



# Task 2: Using the Math Module for Calculations
# 1.   Asks the user for a number as input.
# 2.   Uses the math module to calculate the:
# o    Square root of the number
# o    Natural logarithm (log base e) of the number
# o    Sine of the number (in radians)
# 3.   Displays the calculated results.

import math

# 1. Ask the user for a number
num = float(input("Enter a number: "))

# 2. Use math module to calculate values
sqrt_val = math.sqrt(num)
log_val = math.log(num)       # Natural log (base e)
sine_val = math.sin(num)      # Sine (in radians)

# Print results
print(f"Square root of {num} = {sqrt_val}")
print(f"Natural log (base e) of {num} = {log_val}")
print(f"Sine of {num} radians = {sine_val}")








