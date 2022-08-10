import random

class Pirate:
    #initial variables
    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.critdmg = 0.3
        self.critchance = 18
        self.stamina = 4
        self.health = 100
        self.special_atk = 2

    #shows stats of Pirate
    def show_stats( self ):
        print(f"Pirate Name: {self.name}\nStrength: {self.strength}\nCrit Chance: {self.critchance}\nHealth: {self.health}\n")

    #performs basic attack with chance to crit
    def attack ( self , ninja ):
        bonus_danage = (self.strength * self.critdmg) + self.strength
        roll = random.randint(1,20)
        damage_done = 0
        if roll > self.critchance:
            damage_done = self.strength + bonus_danage
            ninja.health -= damage_done
            print(f"{self.name} performs a critical strike for {damage_done} damage!")
        else:
            damage_done = self.strength
            ninja.health -= damage_done
            print(f"{self.name} attacks for {damage_done} damage.")
        return self

    #heals character for the amount equal to their stamina
    def heal(self):
        print(f"{self.name} is healing for {self.stamina} points of damage")
        self.health += self.stamina
        if self.health > 100:
            self.health = 100
        return self

    #
    def special_attack(self,ninja):
        # berserk: double damage but take 25% hp
        if self.special_atk > 0:
            print(f"{self.name} performs special attack: Berserk!\n {self.strength*2} damage done at the cost of {self.strength} health")
            ninja.health -= self.strength * 2
            self.health -= self.strength
            self.special_atk -= 1
        else:
            print(f"No special attacks remaining. Performing a basic attack instead...\n")
            self.attack(ninja)
        return self
        
