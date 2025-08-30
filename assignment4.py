# ASSIGNMENT 4:
# Module 5: Files, Exceptions, and Errors in Python
# Task 1: Read a File and Handle Errors 
# 1.   Opens and reads a text file named sample.txt.
# 2.   Prints its content line by line.
# 3.   Handles errors gracefully if the file does not exist.
"""f = open("sample.txt","r")
line1 = f.readline()
line2 = f.readline()
print("reading file content : ")
print("line1 : ", line1 )
print("line2 : ", line2)
"""





# Task 2: Write and Append Data to a File
# 1.   Takes user input and writes it to a file named output.txt.
# 2.   Appends additional data to the same file.
# 3.   Reads and displays the final content of the file.


f = open("output.txt","r")
data = f.read()
print("final content of output.txt :\n", data)
