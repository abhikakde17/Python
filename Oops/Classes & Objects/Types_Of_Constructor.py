#Types of Constructor

# 1. Default Constructor (self)
# 2. Parameterized Constructor (self, name, age)
# 3. Constructor with default values (self, name = "unknown", age = 21)#sets  default values as we sets


class Student:
    
    #Default Constructor
    def __init__(self):
        pass
    
    #Parameterized Constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding name in database...")
    
s1 = Student("Abhishek",88)
print(s1.name, s1.marks)

s2 = Student("Aryan",87)
print(s2.name, s2.marks)