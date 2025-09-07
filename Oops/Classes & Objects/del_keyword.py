# del Keyword.

#Used to delete Object properties or Object itself.
# del s1.name
# del s1

class Student:
    def __init__(self,name):
        self.name = name

s1 = Student ("Abhishek")
s2 = Student ("Kakde")
del s1.name


print( s2.name)

