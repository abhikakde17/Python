'''
Write a program to calculate the product of numbers from 1 to 5
'''
product = 1
number = 1

while number<=5:
    product = product*number #Also product*=number
    number+=1
print(product, end=" ")
