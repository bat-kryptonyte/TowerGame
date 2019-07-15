import random
class Deck(Object):
	def __init__(self, size):
		self.tower = list(range(1, size + 1))

	def shuffle(self):
		random.shuffle(self.tower)

	def new_tower(self, size):
		result = self.tower[0:size]
		self.tower = self.tower[size:]
		return result

	def show_card(self):
		return str(self.tower[0])

	def replace(self, index, player_t):
		self.tower[0], player_t[index] = player_t[index], self.tower[0]

	def get_index(self, block):
		return self.tower.index(block)

def display_tower(pt):
		return "This is your deck: " + str(pt)

def is_win(tower):
		return tower == tower.sort()

def main():
	while True:
		deck = Deck(50)
		deck.shuffle()
		pt = deck.new_tower(10)
		vikings = deck.new_tower(10)
		while not is_win(pt) and not is_win(vikings):
			print(display_tower(pt))
			user_input = input("The card you can choose is: " + deck.showCard() + "or you can choose UNKNOWN")
			if user_input.lower() == deck.show_card().lower():
				user_choice = int(input("Please enter the block you wish to switch"))
				deck.replace(deck.get_index(user_choice), pt)
			elif user_input.lower() == "UNKNOWN".lower():
				pass