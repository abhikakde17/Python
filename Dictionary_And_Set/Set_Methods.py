#Set Methods

collection = set() #Returns the empty set.
print(collection)


collection.add("abhi") #Adds an element in a set.
collection.add("abhi")
collection.add(1)
collection.add(222)
collection.add(21)
print(collection)

collection.remove(222) #Removes the element in a set.
print(collection)

collection1 = {"abhi",22,12,12,223,11}
collection1.clear() #Empties the set.
print(collection1)

collection.pop() #Removes a random value
print(collection) 


collection2 = {"kakde","piyusha", 29,9,19}
collection3 = {"Visha", 'Suraj', 19,16,19,'piyusha'}
print(collection3.union(collection2)) #Combines both set values & returns new.

print(collection3.intersection(collection2)) #Combines common values & returns new.
