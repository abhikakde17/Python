'''Develop a simple calculator using Python. The program should:
    - Ask the user to enter two numbers (use `input` function).
    - Store these numbers in two separate variables.
    - Convert the input strings into integers or floats.
    - Calculate and print the sum of these two numbers.
    - For example, if the user enters 5 and 3, the program should print "The sum of 5 and 3 is 8."
    
'''

a = input("Enter a Number: ")
b = input("Enter a Number: ")
  
  
x = float(a)
y = float(b)

sum = x+y

print(f"The Sum Of {x} and {y} is : {sum}")
