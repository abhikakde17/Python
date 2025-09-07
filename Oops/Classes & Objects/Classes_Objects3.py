class Student:
    def set_details(self,name,marks):
        self.name = name
        self.marks = marks
        
    def show_details(self):
        print(f"{self.name} got {self.marks} Marks.")
        
student1 = Student()
student1.set_details("Abhishek", 88)

student2 = Student()
student2.set_details("Piyusha", 97)

student1.show_details()
student2.show_details()