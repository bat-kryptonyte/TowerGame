from Player import player
from anytree import Node, RenderTree, search
class robot1(player):
    def choice(num, tower, ptower, discard_pile, deck):
        pass
    def __minimax(pt, rt, depth, player, discard_pile, deck):
        if player:
            best = []

class node(object):
    def __init__(self, is_leaf, content, children):
        self.is_leaf = is_leaf
        self.content = content
        if is_leaf:
            self.children = None
        else:
            self.children = children


tree = []
tree = RenderTree(tree[0])

def get_available_moves(tower, discard_pile, deck):
        '''Returns [[new_tower, new_discard_pile, new_deck], [], []...]'''
        result = [[tower, [deck[0]] + discard_pile, deck[1:]]]
        for i in range(len(tower)):
            result.append([tower[0:i] + [discard_pile[0]] + tower[i + 1:], [tower[i]] + discard_pile[1:], deck])
            if len(deck) > 0:
                result.append([tower[0:i] + [deck[0]] + tower[i + 1:], [tower[i]] + discard_pile, deck[1:]])
        return result

def generate_tree(pt, rt, discard_pile, deck, node, player):
    tree.append(Node("root", move = [rt, discard_pile, deck]))
    if player:
        lst = get_available_moves(rt, discard_pile, deck)
        for i in range(len(lst)):


def get_score_list(lst, depth, rt, pt, evaluate):
    if depth == 0:
        lst.append(evaluate(rt, pt))
        return
    else:
        pass


tower = [1, 5, 6, 7, 3, 10, 4, 29, 20, 30]
dp = [35, 36, 37]
deck = [14, 17, 2]
print(get_available_moves(tower, dp, deck))
print(tower)
print(dp)
print(deck)