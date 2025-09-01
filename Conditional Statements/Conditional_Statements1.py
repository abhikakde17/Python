'''
Conditional Statements


#Syntax

if(condition1):
    Statement1
elif(condition2):
    Statement2
else:
    StatementN
    
'''

age = int(input("Enter the age : "))

if age >= 18:
    print("You are eligible to vote.")
    
else:
    print("You are not eligible to vote.")