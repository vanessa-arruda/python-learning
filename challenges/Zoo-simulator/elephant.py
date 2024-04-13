from herbivores import Herbivore
import random

class Elephant(Herbivore):
    def __init__(self, name, age, energy, max_energy):
        super().__init__(name, age, energy, max_energy)

    def feed(self, food):
        if self.energy >= self.max_energy:
            print(f"{self.name} don't accept {food}")
            return
        else: 
            self.energy += 2
            print(f"Elephant {self.name} eats {food}. energy is now {self.energy}.")

    def make_sound(self):
        print(f"{self.name} troooooooooomppphhhh with its trunk!")
        return super().make_sound()
    
    def take_action(self, animal_list):
        action = random.choice(self.actions)
        # print(f"{self.name} does {action}.")
        if action == "sleep":
            self.sleep()
        elif action == "play":
            self.play()
        elif action == "feed":
            self.eat()
        elif action == "make sound":
            self.make_sound()
        else:
            print(f"{self.name} is laying close to the pond, sun bathing.")