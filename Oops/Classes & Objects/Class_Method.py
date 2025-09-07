# class Method.

''' 
A class  method is bound to the class & receives the class as an implicit first argument.

NOTE- Static method cannot access or modify class state and generally for utility.
'''

"""Syntax

class Student:
    @classmethod    #decorator
    def college(cls):
    pass

"""

class Person:
    name = "anonymous"
    
    @classmethod
    def changename(cls, name):
        cls.name = name
        
p1 = Person()
p1.changename("Rahul Kumar")
print(p1.name)
print(Person.name)