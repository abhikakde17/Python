#To check the value is odd or even

def odd_even():
    num = int(input("Enter a Number: "))
    if num % 2 ==0:
        print("Even")
    else:
        print("Odd")
        
    return num

user = odd_even()
print(user)