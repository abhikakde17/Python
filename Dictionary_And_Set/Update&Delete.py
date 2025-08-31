'''Create a dictionary named `vehicles`, 
where the keys are different types of vehicles like "Car", "Bike", "Auto", and the values are their colors.

-Update the color of "Bike" in the `vehicles` dictionary to a color of your choice.

-Delete the "Auto" from the `vehicles` dictionary.
'''

Vehicles= {"Car": "Black", "Bike":"Red", "Auto":"Yellow"}

print(Vehicles)

#To Add new value to the dictionary.
Vehicles["Truck"] =  "Red&Black"

#To Update the colour if bike we Updates the colour
Vehicles["Bike"] = "Black"

#To delete the auto from the dictionary we use the del
del Vehicles["Auto"]

print(Vehicles)

#To Access the value of a particular key
colour = Vehicles["Truck"]
print(colour)