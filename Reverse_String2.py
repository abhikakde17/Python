#Reversing String Using For-Loop

string = "I Love Python"

for i in string:
    print(i, end=" ")
print() #For Space


#String Reverse
'''
Slicing
string_name[start: stop: step]

'''

for i in string[: : -1]:
    print(i, end=" ")