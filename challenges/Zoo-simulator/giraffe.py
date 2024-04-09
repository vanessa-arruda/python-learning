from herbivores import Herbivore
import random

class Giraffe(Herbivore):
    def __init__(self, name, age, energy, max_energy):
        super().__init__(name, age, energy, max_energy)

    def feed(self, food):
        if self.energy >= self.max_energy:
            print(f"{self.name} don't accept {food}")
            return
        else: 
            self.energy += 2
            print(f"Giraffe {self.name} eats {food}. energy is now {self.energy}.")

    def make_sound(self):
        print(f"{self.name} makes chomps noises...")
        return super().make_sound()
    
    def take_action(self, animal_list):
        action = random.choice(self.actions)
        if action == "sleep":
            self.sleep()
        elif action == "play":
            self.play()
        elif action == "feed":
            self.eat()
        elif action == "make sound":
            self.make_sound()
        else:
            print(f"{self.name} is curiously looking to the visitors...")