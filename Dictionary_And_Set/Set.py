#Set
'''
- Set is the collection of the unordered items.
- Set is mutable and have unique elements.
- Repeated elements stored only once.
- We can store boolean value,integer,float,string,tuple in a set.
- But we cannot store list and dictionary as they are mutable.
- Sets are unordered.
- Does no return duplicate values.

'''
collection = {1,2,3,"abhi",22.33,True}

print(collection)
print(type(collection))

coll = {1,2,3,2,1,"abhi", 22,"abhi"} #Does not return values which are multiple.
print(coll)