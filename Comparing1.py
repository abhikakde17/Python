#To comparing with the use of STRIP Function

#Start and End with the space.

name = " Abhi Kakde "

#Used the strip function to remove the space at start and at the end.
#lstrip = used to remove space from left side.
#rstrip = used to remove space from right side.
if name.strip() == "Abhi Kakde":
    print("True")
    
else:
    print("False")