'''
Write a program to check a number is prime or not.

'''

num = int(input("Enter a Number: "))

is_prime = True

#We only check the divisors until the sq root of the number so we take range until sq root
for i in range(2, int(num ** 0.5)+1): #Here we calculated the sq root of number 
    if num % i ==0:
        is_prime = False
        break
    
if is_prime and num>1 :
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

