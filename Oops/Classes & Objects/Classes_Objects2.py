class Car:
    def set_details(self,brand,color):
        self.brand = brand
        self.color = color
    
    def show_details(self):
        print(f"This is {self.brand} car with {self.color} colour.")
        
car1 = Car()
car1.set_details("Tata", "Black")

car2 = Car()
car2.set_details("Toyota", "White")

car1.show_details()
car2.show_details()