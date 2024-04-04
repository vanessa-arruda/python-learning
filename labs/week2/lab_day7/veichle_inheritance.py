class Veichle:
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
        print("Fueling tank...")

veichle1 = Veichle("Tesla", "3", "2022")
print(veichle1)

veichle1.start()
veichle1.stop()
veichle1.fuel_up()