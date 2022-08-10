from classes.ninja import Ninja
from classes.pirate import Pirate
import random

# Game flow:---------------------------------------

# Pick pirate or ninja

# Game loop{
# Choose action
# perform action
# Print result
# Loop until someone dies then exit loop
# }

# Print who won
#--------------------------------------------------

#Welcome message------------------------------
print("Welcome to Pirates vs Ninjas!")
selection = input("Enter 1) for Pirate or 2) for Ninja \n> ")

#interpret player character type -----------
if selection == "1":
    player1 = Pirate("Jack Sparrow")
    player2 = Ninja("Snake Eyes")
    print("You chose Pirate!\n!!!!!!!!!!!!!!!!!!!!!!!!!!!\nNPC chose Ninja\n!!!!!!!!!!!!!!!!!!!!!!!!!!!")
else:
    player1 = Ninja("Snake Eyes")
    player2 = Pirate("Jack Sparrow")
    print("You chose Ninja!\n!!!!!!!!!!!!!!!!!!!!!!!!!!!\nNPC chose Pirate\n!!!!!!!!!!!!!!!!!!!!!!!!!!!")

print("May the odds be ever in your favor!\n *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_")
#Main game loop---------------------------------------
while player1.health > 0 and player2.health > 0:
    #choose action
    action = input("Choose an action \n 1) basic attack 2) special attack 3) heal\n >")
    action2 = random.randint(1,3)
    #perform action for player1
    if action == "1":
        player1.attack(player2)
    elif action == "2":
        player1.special_attack(player2)
    else:
        player1.heal()
    #perform action for bot (player2)
    if action2 == 1:
        player2.attack(player1)
    elif action2 == 2:
        player2.special_attack(player1)
    else:
        player2.heal()

    #checks to see if someone died this round
    if player1.health <=0 and player2.health > 0:
        print(f"{player1.name} has died\n {player2.name} is the victor!")
    elif player2.health<=0 and player1.health > 0:
        print(f"{player2.name} has died\n {player1.name} is the victor!")
    elif player1.health < 0 and player2.health < 0:
        print("we have a tie! both players are dead!")

    print("---------------------------\nRound complete! \n--------------------------- \n")
    print("Stats after round \n=============\n")
    #show player stats--------------
    player1.show_stats()
    player2.show_stats()