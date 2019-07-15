from Player import player
from random import random
USER_TOWER_HEIGHT = 10
class random_robot(player):
    def choice(num, tower):
        return random() < 0.5
    
    def get_normal_move(num, tower):
        return int(random() * USER_TOWER_HEIGHT)
    
    def get_question_move(num, tower):
        if random() < 0.5:
            return int(random.random() * USER_TOWER_HEIGHT)
        else:
            return -1
