class Pet:
    def __init__(self,name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 50
        self.energy = 25

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.health += 10
        self.energy += 5
        return self

    def play(self):
        self.health += 5
        print(f"{self.name} does their trick: {self.tricks}")
        return self

    def noise(self):
        if self.type == "cat":
            print("Meoooow!")
        elif self.type == "dog":
            print("WOOOF!")
        elif self.type == "horse":
            print("whinney!")
        else:
            print(f"{self.name} emits a loud noise!")
        return self
    
    def display_stats(self):
        print("----------------")
        print(f"Pet Name: {self.name}")
        print(f"Pet Type: {self.type}")
        print(f"Pet Tricks: {self.tricks}")
        print(f"Pet Health: {self.health}")
        print(f"Pet Energy: {self.energy}")
        print("----------------")
        return self

print("pet imported")
pepper = Pet("Pepper", "dog", "roll over")