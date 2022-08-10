import random

class Ninja:
    #initial variables
    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.critdmg= 0.5
        self.critchance = 15
        self.stamina = 6
        self.health = 100
        self.special_atk = 2
    # shows stats of Ninja
    def show_stats( self ):
        print(f"Ninja Name: {self.name}\nStrength: {self.strength}\nCrit Chance: {self.critchance}\nHealth: {self.health}\n")
    
    #performs basic attack with chance to crit
    def attack ( self , pirate ):
        bonus_danage = (self.strength * self.critdmg) + self.strength
        roll = random.randint(1,20)
        #determine if attack will be a crit or regular
        if roll > self.critchance:
            damage_done = self.strength + bonus_danage
            pirate.health -= damage_done
            print(f"{self.name} performs a critical strike for {damage_done} damage!")
        else:
            damage_done = self.strength
            pirate.health -= damage_done
            print(f"{self.name} attacks for {damage_done} damage.")
        return damage_done
    #heals character for the amount equal to their stamina
    def heal(self):
        print(f"{self.name} is healing for {self.stamina} points of damage.")
        self.health += self.stamina
        if self.health > 100:
            self.health = 100
        return self
    #calls the attack function twice with 2 chances to crit but takes "stamina" worth of damage
    def special_attack(self,pirate):
        #double attack attacks twice takes 1x dmg
        if self.special_atk > 0:
            damage_done = 0
            damage_done += self.attack(pirate)
            damage_done += self.attack(pirate)
            self.health -= self.strength
            print(f"{self.name} performs a special attack: Double attack!\n total damage done was {damage_done} at the cost of {self.strength}")
            self.special_atk -= 1
        else:
            print(f"No special attacks remaining. Performing a basic attack instead...\n")
            self.attack(pirate)
        return self
        

