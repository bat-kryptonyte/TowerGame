import random
USER_TOWER_HEIGHT = 10
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

	def replace(self, index, player_t, x):
		temp = player_t[index]
		player_t[index] = self.tower.pop(0)
		x.get_tower().insert(0, temp)

	def get_index(self, block):
		return self.tower.index(block)
	
	def get_tower(self):
		return self.tower

	def replace_a(self, x):
		x.get_tower().insert(0, self.tower.pop(0))

def display_tower(pt):
		return "This is your deck: " + str(pt)

def is_win(tower):
		return tower == tower.sort()

def main():
	while True:
		tl = int(input("Please enter your tower length: "))
		tower = Deck(tl - 1)
		discardPile = Deck(tl - 1)
		tower.shuffle()
		pt = tower.new_tower(USER_TOWER_HEIGHT)
		vikings = tower.new_tower(USER_TOWER_HEIGHT)
		while not is_win(pt) and not is_win(vikings):
			print(display_tower(pt))
			user_input = input("The card you can choose is: " + discardPile.showCard() + "or you can choose UNKNOWN")
			if user_input.lower() == tower.show_card().lower():
				user_choice = int(input("Please enter the block you wish to switch"))
				discardPile.replace(tower.get_index(user_choice), pt, discardPile)
				print(display_tower(pt))
			elif user_input.lower() == "UNKNOWN".lower():
				print("The card you can choose is: " + tower.showCard())
				u_i = input("Please choose YES, or DISCARD(YOUR TURN WILL BE SKIPPED")
				if u_i.lower() == "YES".lower():
					u_c = input("Please enter the block you wish to switch")
					tower.replace(tower.get_index(u_c, pt), pt, discardPile)
					print(display_tower(pt))
				elif u_i.lower() == "DISCARD".lower():
					tower.replace_a(discardPile)
					print(display_tower(pt))
			step1 = random.random() < 0.5
			step2 = random.random() < 0.5
			rand_v = int(random.random() * USER_TOWER_HEIGHT)
			rand_v2 = int(random.random() * USER_TOWER_HEIGHT)
			if step1:
				discardPile.replace(rand_v, vikings, discardPile)
			else:
				if step2:
					tower.replace(rand_v2, vikings, discardPile)
				else:
					tower.replace_a(discardPile)
		if is_win(pt):
			print("Congratulations! You have won!")
			break
		elif is_win(vikings):
			print("You have lost! Good Luck next time!")
			break