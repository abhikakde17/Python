'''Write a program to calculate the factorial of a given number.'''

n = int(input("Enter a number: "))
factorial = 1
i=1

while i<=n:
    factorial*=i
    i+=1

print(f"Factorial of {n} is {factorial}")