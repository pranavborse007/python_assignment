# ASSIGNMENT 2:
# Module 3: Control Structures in Python
# Task 1: Check if a Number is Even or Odd
# 1. 	Takes an integer input from the user.
# 2. 	Checks whether the number is even or odd using an if-else statement.
# 3. 	Displays the result accordingly.

n = int(input("enter a number : "))
if n%2 == 0:
    print(n, "is an even number. ") 
elif n%2 != 0:
    print(n, "is an odd number")



# Task 2: Sum of Integers from 1 to 50 Using a Loop
# 1.   Uses a for loop to iterate over numbers from 1 to 50.
# 2.   Calculates the sum of all integers in this range.
# 3.   Displays the final sum.

total_sum = 0
i = 1
for i in range(1, 51):
    total_sum +=i

print("the sum of numbers from 1 to 50 is : ", total_sum)







