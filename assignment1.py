# ASSIGNMENT 1:
# Module 2: Basic Python Concepts
# Task 1: Perform Basic Mathematical Operations
# 1.  Takes two numbers as input from the user.
# 2.  Performs the basic mathematical operations on these two numbers:
# o	  Addition
# o	  Subtraction  
# o	  Multiplication
# o	  Division
# 3.  Displays the results of each operation on the screen.

num1 = float(input("enter first number : "))
num2 = float(input("enter second number : "))

print("addition       : " ,num1+num2)
print("Multiplication : " ,num1*num2)
print("Division       : " ,num1/num2)
print("Subtraction    : " ,num1-num2)


# Task 2: Create a Personalized Greeting
# 1.  Takes a user's first name and last name as input.
# 2.  Concatenates the first name and last name into a full name.
# 3.  Prints a personalized greeting message using the full name.

firstname = input("enter your first name : ")
lastname = input("enter your last name : ")
print("hello, ", firstname , lastname , "!","welcome to python programm.")