#Conditional Statements

total = int(input("Enter the Total Shopping Cost: "))

if total>=10000:
    print("You Are Eligible For the 50% Discount.")
    
elif total>=1 and total<=9999:
    print("You are not eligible for the discount.")
    
else:
    print("Please re-enter right amount.")
