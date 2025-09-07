#Constructor


class Car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
        
car1 = Car("Volkswagen", "Black") #Sets values automatically

print(car1.brand,car1.color)