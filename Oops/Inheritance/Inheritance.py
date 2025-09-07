#Inheritance

'''
When one class(child/derived) derives the properties and methods of another class(Parents/Base)

class Car:
    ....

class ToyotaCar(Car):
    ....
    
'''

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