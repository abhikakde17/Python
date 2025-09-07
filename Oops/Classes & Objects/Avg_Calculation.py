'''Create student class that takes name & marks of 3 subjects as arguments in constructor.
Then create a method to print the average.'''

class Student():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print(f"Hi {self.name} your average score is {sum/3}")
        
s1 = Student("Abhi",[99,98,95])
s1.avg()
