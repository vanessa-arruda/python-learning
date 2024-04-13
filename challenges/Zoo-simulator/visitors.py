import random
from carnivores import Carnivore
from herbivores import Herbivore

class Visitor:
    actions = ["observe", "feed", "play"]
    def __init__(self, name, age):
        self.name = name
        self.age = age
      
    # def observe(self, animals_list):
    def observe(self, animals_list):
        while True:
            animal_index = random.randint(0, len(animals_list) - 1)
            if isinstance(animals_list[animal_index], Visitor):
                print(f"{self.name} is searching for an animal to observe...")
            else:
                print(f"{self.name} is observing {animals_list[animal_index].get_name()}, the {(animals_list[animal_index].__class__.__name__).lower()}, from the fences")
                break
    def get_name(self):
        return self.name

    def feed(self, animals_list):
        animal_index = random.randint(0, len(animals_list)-1)
        if isinstance(animals_list[animal_index], Herbivore):
            print(f"{self.name} feeds {animals_list[animal_index].name}, the {animals_list[animal_index].__class__.__name__.lower()}")
            animals_list[animal_index].eat()
        else:
            print(f"{self.name} is on the queue to feed an animal...")

    def play(self, animals_list):
        animal_index = random.randint(0, len(animals_list)-1)
        if isinstance(animals_list[animal_index], Visitor) and animals_list[animal_index] != self.name:
            print(f"{self.name} runs around the park with {animals_list[animal_index].get_name()}.")
        elif isinstance(animals_list[animal_index], Herbivore):
            print(f"{self.name} plays with {animals_list[animal_index].get_name()}, the {animals_list[animal_index].__class__.__name__.lower()}.")
            animals_list[animal_index].play()
        else:
            print(f"{self.name} tried, but couldn't play with the lions now.")
    
    def take_photo(self, animals_list):
        animal_index = random.randint(0, len(animals_list)-1)
        print(f"{self.name} took a photo of {animals_list[animal_index].get_name()}, the {animals_list[animal_index].__class__.__name__.lower()}.")

    #function to control all active/passive actions with this class
    def take_action(self, animals_list):
        action = random.choice(self.actions)
        # print(f"{self.name} does {action}")
        if action == "observe":
            self.observe(animals_list)
        elif action == "feed":
            self.feed(animals_list)
        elif action == "play":
            self.play(animals_list)
        else:
            self.take_photo(animals_list)