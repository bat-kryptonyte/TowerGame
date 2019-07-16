from Player import player
from anytree import Node, RenderTree, search
class robot1(player):
    def choice(num, tower, ptower, discard_pile, deck):
        pass
    def __minimax(pt, rt, depth, player, discard_pile, deck):
        if player:
            best = []

tree = []
namelist = list(range(21 ** 5))

def get_available_moves(tower, discard_pile, deck):
        '''Returns [[new_tower, new_discard_pile, new_deck], [], []...]'''
        if len(deck) > 0:
            result = [[tower, [deck[0]] + discard_pile, deck[1:]]]
        else:
            result = []
        for i in range(len(tower)):
            result.append([tower[0:i] + [discard_pile[0]] + tower[i + 1:], [tower[i]] + discard_pile[1:], deck])
            if len(deck) > 0:
                result.append([tower[0:i] + [deck[0]] + tower[i + 1:], [tower[i]] + discard_pile, deck[1:]])
        return result

def generate_tree(pt, rt, discard_pile, deck, node, player, p):
    if player:
        p_node = Node(str(namelist.pop(0)), parent = p, move = [rt, discard_pile, deck])
        tree.append(p_node)
        if node == 0:
            return
        lst = get_available_moves(rt, discard_pile, deck)
        print(lst)
        for m in lst:
            generate_tree(pt, m[0], m[1], m[2], node - 1, False, p_node)
    else:
        p_node = Node(str(namelist.pop(0)), parent = p, move = [pt, discard_pile, deck])
        tree.append(p_node)
        if node == 0:
            return
        lst = get_available_moves(pt, discard_pile, deck)
        for m in lst:
            generate_tree(m[0], rt, m[1], m[2], node - 1, True, p_node)


def get_score_list(lst, depth, rt, pt, evaluate):
    if depth == 0:
        lst.append(evaluate(rt, pt))
        return
    else:
        pass

rt = [46, 29, 5, 36, 44, 23, 42, 40, 26, 48]
discard = [24]
deck = [10, 22, 21, 39, 43, 14, 6, 35, 41, 11, 4, 28, 32, 33, 18, 13, 37, 16, 47, 38, 50, 3, 25, 31, 2, 49, 1, 20, 17]
pt = [12, 34, 7, 8, 30, 45, 9, 27, 19, 15]
#print(get_available_moves(rt, discard, deck))
generate_tree(pt, rt, discard, deck, 2, True, None)
t = RenderTree(tree[0])
print(t)