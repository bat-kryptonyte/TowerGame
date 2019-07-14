import random
def is_win(tower):
    return tower == tower.sort()

deck = list(range(1, 51))
random.shuffle(deck)
player_deck = deck[:10]
viking_deck = deck[10:20]