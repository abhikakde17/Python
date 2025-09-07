#STATIC METHOD

#Methods that don’t use the self parameter (work at class level)

'''
class Student:
    @staticmethod   #Decorator
    def college( ):
        print( “ABC College” )
'''
class Student():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    @staticmethod
    def hello():
        print("Hello")
        
        
s1 = Student("Abhi",[99,98,95])
s1.hello()
print(s1.name, s1.marks)
