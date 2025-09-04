'''
define a function, 
take 5 inputs numbers from the user, put it in a list 
and sum the numbers.

'''
def sum():
    lst =[]
    user = int(input("Enter how many number you want to add : "))

    for i in range(user):
        choice = int(input(f"Enter the element {i}: "))
        lst.append(choice)

    #For the addtion of these elements
    total = 0
    for i in range(len(lst)):
        total +=lst[i]#Adds the value at each index position in list
    return f"Total is {total}"

s = sum()
print(s)
