players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32,
        "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33,
        "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32,
        "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    },
    {
        "name": "Carl Malone",
        "age": 59,
        "position": "Power Forward",
        "team": "Utah Jazz"
    }
]
from operator import ne
import random

kevin = {
        "name": "Kevin Durant 2", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
}
jason = {
        "name": "Jason Tatum 2", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
}
kyrie = {
        "name": "Kyrie Irving 2", 
        "age":32,
        "position": "Point Guard", 
        "team": "Brooklyn Nets"
}
    
# Create your Player instances here!
# player_jason = ???


# challenge 1: update the constructor to accept a dictionary with a single players information istead of individual arguments for the attributes
class Player:
    roster = []
    def __init__(self, player_dict):
        self.name = player_dict["name"]
        self.age = player_dict["age"]
        self.position = player_dict["position"]
        self.team = player_dict["team"]
        Player.roster.append(self)
    
    def try_for_two(self):
        rand = random.randrange(0,2)
        if rand == 1:
            print("He shoots, he scores!")
        elif rand == 0:
            print("He shoots he misses")
    
    def player_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Position: {self.position}")
        print(f"Team: {self.team}")
        print("-------------------------")
        # return self

    @classmethod
    def print_roster(cls):
        print("Players in the roster:")
        for team_player in cls.roster:
            print(team_player.name)
    
    @classmethod
    def get_team(cls, team_list):
        new_team = []
        for index in range(len(team_list)):
            new_team.append(Player(team_list[index]))
        return new_team


player_kevin = Player(kevin),
player_jason = Player(jason)
player_kyrie = Player(kyrie)

new_list = Player.get_team(players)
print("new list roster")
for index in range(len(new_list)):
    new_list[index].player_info()
print("end of new list roster")

# Player.print_roster()