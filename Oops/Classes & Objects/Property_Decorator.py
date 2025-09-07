#Property Decorator

'''We use @property decorator on any method in the class to use the method as a property.'''

class Student:
    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
        
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.maths) / 3) + "%"
    
stu1 = Student(98,99,97)
print(stu1.percentage)

stu1.phy = 95
print(stu1.percentage)