#To print the table of the given number.

'''
2
2*1 = 2
2*2 = 4
2*3 = 6

(number) * (x) = (number * x)

'''



number = int(input("Enter a number: "))

x = 1

while x<=10:
    print(f"{number} * {x} = {number * x}")
    x+=1