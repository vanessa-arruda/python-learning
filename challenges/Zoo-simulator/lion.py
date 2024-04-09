from carnivores import Carnivore
import random

class Lion(Carnivore):
    def __init__(self, name, age, energy, max_energy):
        super().__init__(name, age, energy, max_energy)

    #override
    def make_sound(self):
        print("Groooooaaaarr!")
        return super().make_sound()
  
    def take_action(self, animals_list):
        action = random.choice(self.actions)
        # print(f"{self.name} does {action}")
        if action == "hunt":
            self.hunt(animals_list)
        elif action == "sleep":
            self.sleep()
            print("Lion starts dreaming: '...In the jungle, the mighty jungle, the lion sleeps tonight'...")
        elif action == "play":
            self.play()
        elif action == "feed":
            self.eat()
        elif action == "make_sound":
            self.make_sound()
        else:
            print(f"{self.name} lays down under the tree doing nothing.")
    