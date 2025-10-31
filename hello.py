#second commit 
class Car:
    def __init__(self,make, model, year):
        self.make = make
        self.model = model
        self.year = year 

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

    def start(self):
        print(f"The {self.make} {self.model} is now running")

    
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Telsa", "model 3", 2023)


car1.display_info()
car1.start()

car2.display_info()
car2.start()

        
