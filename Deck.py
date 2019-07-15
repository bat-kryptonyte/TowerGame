import random
class Deck(Object):
	def __init__(self, size):
		self.tower = list(range(1, size + 1))

	def new_tower(self, size):
		result = self.tower[0:size]
		self.tower = self.tower[size:]
		return result

	def show_card(self):
		print("The card you can choose is: " + str(self.tower[0])

	def replace(self, index, player_t):
		self.tower[0], player_t[index] = player_t[index], self.tower[0]

	def display_tower(self, pt):
		return "This is your deck: " + str(pt)
