class Animal:
  
  def __init__(self, name, age, energy, max_energy):
    self.name = name
    self.age = age
    self.max_energy = max_energy
    self.energy = energy
    self.actions = ["sleep", "play", "feed", "make sound"]
    #conditional to not allow energy above max energy
    if self.energy > max_energy:
      self.energy = max_energy
    print(f"{self.name} is a current energy is {self.energy}")
  def eat(self, food):
    print(f"{self.name} is eating {food}...")
    if self.energy >= self.max_energy:
      print(f"{self.name} is not hungry now")
    else: 
      self.energy += 1
      print(f"The {food} is delicious. Nhom, Nhom! {self.name}'s energy increases to {self.energy}.")

  def sleep(self):
    self.energy += 2
    print(f"{self.name} is tired and goes sleep - ZzZz... energy increases to {self.energy}")

  def play(self):
    self.energy -= 2
    if self.energy <= 0:
      print(f"Oh no! {self.name} died. Energy level went to 0.")
    else:
      print(f"Weeee! {self.name} is happy for playing! energy drops to {self.energy}...")

  def make_sound(self):
    pass

