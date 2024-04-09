#base class
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"This is a {self.brand}, model {self.model}, year {self.year}"
    
    def start(self):
            print("Blip! Enginee started!")
    
    def stop(self):
        print("Blip! Enginee stopped!")

    def fuel_up(self):
        print("Fueling tank...\n")

# Derived class  - inheret functionalities of Veichle
class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors
    
    def __str__(self):
        return f"{super().__str__()}, with 4 doors\n"
    
    def honk_horn():
        print("Biiip, Biiiiiip!\n")

class Bicycle(Vehicle):
    def __init__(self, brand, model, year, num_gears):
        super().__init__(brand, model, year)
        self.num_gears = num_gears

    def __str__(self):
        return f"{super().__str__()}, {self.num_gears} gears\n"
    
    def ring_bell():
        print("plin, plin!\n")

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)
    
    def __str__(self):
        print("Ran, Ran, dan dan dan dan!\n")
        return f"{super().__str__()}"
        

# objects creation
vehicle1 = Car("Tesla", 3, "2022", 4)
vehicle2 = Vehicle("Volvo", "XC60", "2024")
vehicle3 = Bicycle("Caloi", "XT Runner", "2019", 21)
vehicle4 = Motorcycle("Harley & Davison", "Night Rock", "2023")
print(vehicle1)

vehicle1.start()
vehicle1.stop()
vehicle1.fuel_up()

print(vehicle2)
print(vehicle3)
print(vehicle4)