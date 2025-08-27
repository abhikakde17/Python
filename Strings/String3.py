'''Create a Python program that prompts the user to enter their age in years using the `input` function.
Convert this age from a string to an integer and store it in a variable. 
Then, calculate and print the age in months (assume 12 months in a year). 
For example, if the user enters "20", the program should output "You are 240 months old."
'''

name = input("Enter Your Name: ")
age =  input("Enter Your Age: ")

#Converting the string age into the integer.
age1 = int(age)

#To Calculate Age In Months.
age2 = age1 * 12

#Printing Using F-String.
print(f"{name} is {age2} months old.")

