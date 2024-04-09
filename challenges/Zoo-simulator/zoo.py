import random
from visitors import Visitor
from animal import Animal
from carnivores import Carnivore
from herbivores import Herbivore
from monkey import Monkey
from lion import Lion

def start_simulation():
    print("----------------------------------------------------------------------------\n")
    print("                     WELCOME TO VÄRLDEN ZOO SIMULATOR\n")
    print("----------------------------------------------------------------------------")
    print(f"\nWelcome! Today is going to be a FUN DAY at VÄRLDENS ZOO!\n")
    print(f"It's a beautiful sunny morning... the visitors start entering the park...\n\n")
    print(f"...It will happen a lot today...\n")

    print(f"---- Animals at the zoo ----\n")
    #generate visitors
    v1 = Visitor("Marie", 7)
    v2 = Visitor("Giovanna", 18)
    v3 = Visitor("Leo", 5)
    v4 = Visitor("Vincent", 8)
    v5 = Visitor("Peter", 36)
    v6 = Visitor("Joanna", 32)
    visitor_list = [v1, v2, v3, v4, v5, v6]

    #generate animals
    monk1 = Monkey("Gong", 12, 20, 20)
    monk2 = Monkey("Chipa", 10, 18, 20)
    monk3 = Monkey("Kong", 17, 17, 20)

    lion1 = Lion("Mufasa", 7, 25, 30)
    lion2 = Lion("Sarabi", 6, 20, 30)

    monkey_list = [monk1, monk2, monk3]
    lion_list = [lion1, lion2]
    actors_list = visitor_list + monkey_list + lion_list
    hour_time = 9
    open_time = 8
    for _ in range(open_time):
          #first put hours for each turn of the simulation
        hour_time += 1
        if hour_time == 10:
            print(f"--------------------------- It's {hour_time}:00, Zoo is open! -----------------------------")
        elif  hour_time == 17:
            print(f"------------------------ It's {hour_time}:00, Zoo closes in 1 hour! -----------------------")
        else:
            print(f"---------------------------- Hour of the day: {hour_time}:00 ------------------------------")
        for actor in actors_list:
            actor.take_action(actors_list)
    print(f"----------------------------------- Zoo is now closed! ------------------------------------")
    print(f"All visitors go home and the animals go rest for the day...")
    print(f"-------------------------------------------------------------------------------------------")
start_simulation()