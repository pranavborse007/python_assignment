# ASSIGNMENT 5:
# Module 6: Data Structures and Strings in Python
# Task 1: Create a Dictionary of Student Marks
# 1.   Creates a dictionary where student names are keys and their marks are values.
# 2.   Asks the user to input a student's name.
# 3.   Retrieves and displays the corresponding marks.
# 4.   If the student’s name is not found, display an appropriate message.

students = {"pranav" : 65, "mohit" : 98, "shantanu" : 76, "dipak" : 54}
studentname = input("enter the student's name: ")
if studentname in students:
    print(studentname+"'s marks : " , students[studentname])
else:
    print("student not found")




# Task 2: Demonstrate List Slicing 
# 1.   Creates a list of numbers from 1 to 10.
# 2.   Extracts the first five elements from the list.
# 3.   Reverses these extracted elements.
# 4.   Prints both the extracted list and the reversed list

# Step 1: Create a list of numbers from 1 to 10
numbers = list(range(1, 11))

# Step 2: Extract the first five elements
extracted = numbers[:5]

# Step 3: Reverse the extracted elements
reversed_list = extracted[::-1]

# Step 4: Print both lists
print("Extracted list:", extracted)
print("Reversed list:", reversed_list)
















