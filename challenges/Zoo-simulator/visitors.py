import random
from carnivores import Carnivore
from herbivores import Herbivore

class Visitor:
    actions = ["observe", "feed", "play"]
    def __init__(self, name, age):
        self.name = name
        self.age = age
      
    def observe(self, animals_list):
        animal_index = random.randint((0, len(animals_list)-1))
        while animals_list[animal_index].isinstance(Visitor) == True:
            print(f"{self.name} is searching for an animal to observe...")
        else:
            print(f"{self.name} is observing {animals_list[animal_index].__class__.__name__} from the fences")

    #function to control all active/passive actions with this class
    def take_action(self, animals_list):
        action = random.choice(self.actions)
        print(f"{self.name} does {action}")
        # if action == "observe":
        #     self.observe()
        # elif action == "feed":
        #     animal_index = random.randint((0, len(animals_list)-1))
        #     if animals_list[animal_index].isinstance(Herbivore) != True:
        #         print(f"{self.name} is on the queue to feed an animal...")
        #     else:
        #         animal_index = random.randint((0, len(animals_list)-1))
        #         print(f"{self.name} feeds {animals_list[animal_index].__name__}")
        #         animals_list[animal_index].eat()
        # elif action == "play":
        #     animal_index = random.randint((0, len(animals_list)-1))
        #     if animals_list[animal_index].isinstance(Visitor) == True:
        #         print(f"{self.name} runs around with {animals_list[animal_index].__name__}")
        #     elif animals_list[animal_index].isinstance(Herbivore) == True:
        #         print(f"{self.name} plays with {animals_list[animal_index].__name__ }")
        #         animals_list[animal_index].play()
        #     else:
        #         print(f"Oh no! {self.name} tried to play with {animals_list[animal_index].__name__ } without success...")