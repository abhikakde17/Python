'''
Write a program to print all odd numbers from 1 to 100

'''

number = 1

while number<=100:
    if number%2!=0:
        print(number, end=" ")
    number+=1