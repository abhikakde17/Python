'''
Write a program to print the first 10 terms of the Fibonacci sequence.

'''

#Fibonacci sequence is the sum of the two preceding ones.

#Fixed  first two terms are 0 and 1

a = 0
b = 1

print(a,b, end=" ")


for _ in range (8): #Here we used _ as a temperory variable in python and range is 8 as already 2 terms are defined.
    next_term = a + b
    print(next_term, end=" ")
    a,b = b,next_term #Here we assign the value of a to b and b to the next term
    
    