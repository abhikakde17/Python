'''
Take a list as an input,
return the maximum value and the minimumm value

'''

def value():
    lst = []
    user = int(input("Enter how many no. of elements you want: "))

    for i in range(user):
        add = int(input(f"Enter the no. {i}: "))
        lst.append(add)
    print(lst)

    #To get maximum value
    maximum = max(lst)
    print(f"Maximum value is {maximum}")

    minimum = min(lst)
    print(f"Minimum value is {minimum}")

value()
