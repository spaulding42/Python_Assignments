class Player:
    def __init__(self,data):
        self.lives = data['lives']
        self.sound = True
        self.score = 0
        self.levels_won = []
        self.powerups = []