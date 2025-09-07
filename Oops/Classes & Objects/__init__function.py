#__init__ Funtion
'''
All classes have a function called __init__(), 
which is always executed when the object is being
initiated.
'''

#Creating Class
'''
class Student:
    def __init__(self, fullname):
        self.name = fullname
'''
#Creating Object
'''
s1 = Student("Abhishek")
print(s1.name)

'''

class Student:
    def __init__(self, name):
        self.name = name
        print("Adding name in database...")
    
s1 = Student("Abhishek")
print(s1.name)

s2 = Student("Aryan")
print(s2.name)