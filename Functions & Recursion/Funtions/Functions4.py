# To draw the pattern 

def lines():
    line = int(input("Enter the number of lines: "))
    for i in range (1,line+1):
        for j in range (i):
            print("*", end=" ")
        print()
        
    return f"The {line} number of triangle has been created."

triangle = lines()
print(triangle)