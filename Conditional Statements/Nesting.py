#Nesting

#Nesting is if-else statement inside a other if-else statement.

age = int(input("Enter the age: "))

if age >= 18:
    if age>= 80:
        print("Cannot drive.")
    else:
        print("Can drive")
        
else:
    print("Your are a minor you cannot drive.")