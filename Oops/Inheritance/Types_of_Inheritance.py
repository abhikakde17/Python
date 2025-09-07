#Types Of Inheritance
'''
1.Single Inheritance.
2.Multi-Level Inhertiance.
3.Multiple Inheritance.
'''

#Single Inheritance.

class Car:
    @staticmethod
    def start():
        print("Car Started...")
        
    @staticmethod
    def stop():
        print("Car Stopped.")
        
class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name
        
car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Innova")

print(car1.name)
print(car2.name)

#Multi-Level Inheritance.

class Car:
    @staticmethod
    def start():
        print("Car Started...")
        
    @staticmethod
    def stop():
        print("Car Stopped.")
        
class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand = brand
        
class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type
        
car1 = Fortuner("Diesel")
car1.start()
        

#Multiple Inheritance.

class A:
    varA = 'Welcome to class A'
    
class B:
    varB = 'Welcome to class B'
    
class C(A, B):
    varC = 'Welcome to class C'
    
c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)