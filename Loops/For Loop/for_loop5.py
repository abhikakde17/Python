
x = int(input("Enter the starting number: "))
y = int(input("Enter the end number: "))
z = int(input("Enter the no with divisble by: "))

for i in range(x,y):
    if i % z == 0:
        print(i)