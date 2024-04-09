from animal import Animal

class Herbivore(Animal):
    def __init__(self, name, age, energy, max_energy):
        super().__init__(name, age, energy, max_energy)
        self.actions.append("run around")
    # overriding from Animal.
    def eat(self):
        super().eat("fruit")

    def run_around(self):
        print(f"{self.name} is running around")

    #create play() with others (visitors/herbivores)




