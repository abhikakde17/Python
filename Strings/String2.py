'''Write a Python program that asks the user for their name using the `input` function.
Store the name in a variable, and then print a greeting message that includes the name.
For example, if the user enters "Ankit", the program should print "Hello, Ankit!".'''


name = input("Enter Your Name: ")

print("Good Morning!", name)

#Using F-string 
print(f"Good Morning, {name}!")