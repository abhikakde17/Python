#Dictionary Methods

myDict = {"name":"Abhi",
           "age": 22,
           "education": "Btech"
           }
new_dict ={"age":23, "city":"Pune"}
print(myDict)

print(myDict.keys()) #Returns all the keys.

print(myDict.values()) #Returns all values.

print(myDict.items()) #returns all (key, val) pairs as tuples

print(myDict.get( "age" )) #Returns the key according to value.

(myDict.update(new_dict)) ##inserts the specified items to the dictionary
print(myDict)
