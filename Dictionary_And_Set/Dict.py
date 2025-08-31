#Dictionary

'''Dictionaries are used to store data values in key:value pairs
“key” : value

They are unordered, mutable(changeable) & don’t allow duplicate keys
'''

dict= {"name" : "abhi",
        "cgpa": 7.5,
        "marks": [75,80,88]
} 
dict["age"] = 20 #To assign or add new value.
print(dict)

#Nested Dictionary

student = {
    "name" : "Abhishek",
    "Score" : {
        "Phy":85,
        "Eng":88,
        "Maths":90
    },
    "age":22
}
print(student)