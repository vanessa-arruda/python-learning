from carnivores import Carnivore
import random

class Tiger(Carnivore):
    def __init__(self, name, age, energy, max_energy):
        super().__init__(name, age, energy, max_energy)

    #override
    def make_sound(self):
        print("Groooooaaaarr!")
        return super().make_sound()
  
    def take_action(self, animals_list):
        action = random.choice(self.actions)
        if action == "hunt":
            self.hunt(animals_list)
        elif action == "sleep":
            self.sleep()
        elif action == "play":
            self.play()
        elif action == "feed":
            self.eat()
        elif action == "make_sound":
            self.make_sound()
        else:
            print(f"{self.name} is sun bathing close to the visitors.")