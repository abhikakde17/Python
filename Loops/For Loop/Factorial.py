'''
Write a program to calculate the factorial of a given number.

'''
n = int(input("Enter the to calculate factorial: "))
factorial = 1

for i in range(1, n+1):
    factorial *= i
    
print(f"Factorial of the {n} is {factorial} ")