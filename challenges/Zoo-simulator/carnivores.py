import random
from animal import Animal
from herbivores import Herbivore

class Carnivore(Animal):
    def __init__(self, name, age, energy, max_energy):
        super().__init__(name, age, energy, max_energy)
        self.actions.append("hunt")

    def eat(self):
        super().eat("meat")

    #active action
    def hunt(self, animals_list):
        if self.energy <= 10:
          prey_index = random.randint(0, len(animals_list)-1)
          if isinstance(animals_list[prey_index], Herbivore):
            print(f"{self.name} is starving and starts hunting {animals_list[prey_index].get_name()}")
            print(f"{animals_list[prey_index].get_name()} is dead")
            animals_list.pop(prey_index)
          else:
            print(f"Tried hunting a {(animals_list[prey_index].__class__.__name__).lower()} but failed.")
      

