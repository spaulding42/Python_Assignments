from ninja_class import ninja1
from pet_class import Pet

class Dog(Pet):
    def __init__(self, name, type, tricks):
        super().__init__(name, type, tricks)
        self.breed = "Mutt"
    
    def display_stats(self):
        print("----------------")
        print(f"Pet Name: {self.name}")
        print(f"Pet Type: {self.type}")
        print(f"Dog Breed: {self.breed}")
        print(f"Pet Tricks: {self.tricks}")
        print(f"Pet Health: {self.health}")
        print(f"Pet Energy: {self.energy}")
        print("----------------")
        return self

ninja1.feed().walk().bathe()

ninja1.pet.display_stats()

my_dog = Dog("Fido","dog", "roll over")
my_dog.breed = "boston terrier"

my_dog.display_stats()

