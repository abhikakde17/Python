
''' Write a program to find the greatest of 3 numbers entered by the user.'''

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

if num1>num2 and num1>num3:
    print(f"{num1} is greater number.")

elif num2>num3:
    print(f"{num2} is greater number.")
    
else:
    print(f"{num3} is greater number.")
