class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
        
#Creating objects
student1 = Student("Abhi", 21, "A+")
student2 = Student("Aryan", 21, "O+")
student3 = Student("Piyusha", 22, "O")

print(student1.name, student1.age, student1.grade)
print(student2.name, student2.age, student2.grade)
print(student3.name, student3.age, student3.grade)