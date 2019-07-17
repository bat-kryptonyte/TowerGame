from Player import player
from numba import jit
from math import inf
import time
class robot1(player):
    def choice(num, tower, ptower, discard_pile, deck):
        pass
    def __minimax(pt, rt, depth, player, discard_pile, deck):
        if player:
            best = []

class node(object):

    def __init__(self, pt, rt, discard_pile, deck, player):
        self.player = player
        self.lst = [discard_pile, deck]
        self.rt = rt
        self.pt = pt

    def get_rt(self):
        return self.rt
    
    def get_pt(self):
        return self.pt

    def get_discard(self):
        return self.lst[0]

    def get_deck(self):
        return self.lst[1]
    
    def is_robot(self):
        return self.player

def generate_subnode(n):
        '''Returns [[new_tower, new_discard_pile, new_deck], [], []...]'''
        discard_pile = n.get_discard()
        deck = n.get_deck()
        if n.is_robot():
            tower = n.get_pt()
            rt = n.get_rt()
            if len(deck) == 0:
                return []
            result = [node(tower[:], rt, [deck[0]] + discard_pile[:], deck[1:], not n.is_robot())]
            for i in range(len(tower)):
                result.append(node(tower[0:i] + [discard_pile[0]] + tower[i + 1:], rt, [tower[i]] + discard_pile[1:], deck, not n.is_robot()))
                if len(deck) > 0:
                    result.append(node(tower[0:i] + [deck[0]] + tower[i + 1:], rt, [tower[i]] + discard_pile, deck[1:], not n.is_robot()))
        else:
            tower = n.get_rt()
            pt = n.get_pt()
            if len(deck) == 0:
                return []
            result = [node(pt, tower[:], [deck[0]] + discard_pile[:], deck[1:], not n.is_robot())]
            for i in range(len(tower)):
                result.append(node(pt, tower[0:i] + [discard_pile[0]] + tower[i + 1:], [tower[i]] + discard_pile[1:], deck, not n.is_robot()))
                if len(deck) > 0:
                    result.append(node(pt, tower[0:i] + [deck[0]] + tower[i + 1:], [tower[i]] + discard_pile, deck[1:], not n.is_robot()))
        return result
'''
def generate_tree(pt, rt, discard_pile, deck, node, player, p):
    if player:
        p_node = Node(str(namelist.pop(0)), parent = p, move = [rt, discard_pile, deck])
        tree.append(p_node)
        if node == 0:
            return
        lst = get_available_moves(rt, discard_pile, deck)
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
'''
def count_order(playerTower):
	temp = []
	count = 0
	max = 0
	alst = []
	lst = [playerTower[0]]
	i = 1
	for y in range(len(playerTower) - 1):
		if(playerTower[y] > playerTower[y + 1]):
			lst.append(playerTower[y])
			temp = lst
			alst.append(temp)
			lst = []
		else:
			lst.append(playerTower[y])
	for x in range(len(alst) - 1):
		if(len(alst[x]) < len(alst[x + 1])):
			max = len(alst[x + 1])
	return (max + 1)/10 * 100

def evaluate(n):
    playerTower = n.get_pt()[:]
    vikingTower = n.get_rt()[:]
    x = count_order(playerTower)
    y = count_order(vikingTower)
    return y - x
'''
def minimax(current_node, depth, evaluate):
    if depth == 0:
        return evaluate(current_node)
    if not current_node.is_robot():
        value = -inf
        for n in generate_subnode(current_node):
            value = max(value, minimax(n, depth - 1, evaluate))
        return value
    else:
        value = inf
        for n in generate_subnode(current_node):
            value = min(value, minimax(n, depth - 1, evaluate))
        return value
'''
def minimax(current_node, depth, alpha, beta, evaluate):
    if depth == 0:
        return evaluate(current_node)
    if not current_node.is_robot():
        value = -inf
        for n in generate_subnode(current_node):
            value = max(value, minimax(n, depth - 1, alpha, beta, evaluate))
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return value
    else:
        value = inf
        for n in generate_subnode(current_node):
            value = min(value, minimax(n, depth - 1, alpha, beta, evaluate))
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value

def main():
    rt = [20, 29, 30, 36, 44, 23, 42, 40, 26, 48]
    discard = [24]
    deck = [10, 22, 21, 39, 43, 14, 6, 35, 41, 11, 4, 28, 32, 33, 18, 13, 37, 16, 47, 38, 50, 3, 25, 31, 2, 49, 1, 20, 17]
    pt = [12, 34, 7, 8, 30, 45, 9, 27, 19, 15]
    nd = node(pt, rt, discard, deck, True)
    #print(evaluate(nd))
    t = time.time()
    print(minimax(nd, 8, -inf, inf, evaluate))
    print(time.time() - t)

#print(get_available_moves(rt, discard, deck))
'''
generate_tree(pt, rt, discard, deck, 4, True, None)
print("finish generating")
#t = RenderTree(tree[0])
print(len(tree))
'''
main()