'''
Write a program to calculate 3 to the power of 4
'''

base_value = int(input("Enter the base value: "))
exponent_value = int(input("Enter the exponent value: "))
count = 0
result = 1

while count < exponent_value:
    result *= base_value
    count+=1
print(f"The {base_value} to the power of {exponent_value} is : {result}")