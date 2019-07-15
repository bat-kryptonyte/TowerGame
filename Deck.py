import random
USER_TOWER_HEIGHT = 10
class Deck(object):
	def __init__(self, size):
		self.tower = []
		for i in range(1, size + 1):
			self.tower.append(i)

	def shuffle(self):
		random.shuffle(self.tower)

	def new_tower(self, size):
		result = []
		for i in range(size):
			result.append(self.tower.pop(0))
		return result

	def show_card(self):
		return str(self.tower[0])

	def replace(self, index, player_t, x):
		temp = player_t[index]
		player_t[index] = self.tower.pop(0)
		x.get_tower().insert(0, temp)

	def get_tower(self):
		return self.tower

	def replace_a(self, x):
		x.get_tower().insert(0, self.tower.pop(0))

def display_tower(pt):
		return "This is your deck: " + str(pt)

def is_win(tower):
		return tower == tower[:].sort()

def get_index(block, pt):
		return pt.index(block)

def main():
	while True:
		tl = int(input("Please enter your tower length: "))
		tower = Deck(tl)
		tower.shuffle()
		pt = tower.new_tower(USER_TOWER_HEIGHT)
		vikings = tower.new_tower(USER_TOWER_HEIGHT)
		discardPile = Deck(0)
		tower.replace_a(discardPile)
		print(display_tower(pt))
		while not is_win(pt) or not is_win(vikings):
			user_input = input("The card you can choose is: " + discardPile.show_card() + "or you can choose UNKNOWN")
			if user_input.lower() == discardPile.show_card().lower():
				user_choice = int(input("Please enter the block you wish to switch"))
				discardPile.replace(get_index(user_choice, pt), pt, discardPile)
				print(display_tower(pt))
			elif user_input.lower() == "UNKNOWN".lower():
				print("The card you can choose is: " + tower.show_card())
				u_i = input("Please choose YES, or DISCARD(YOUR TURN WILL BE SKIPPED")
				if u_i.lower() == "YES".lower():
					u_c = int(input("Please enter the block you wish to switch"))
					tower.replace(get_index(u_c, pt), pt, discardPile)
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
			again = input("Would you like to play again(YES or NO)")
			if again.lower() == "YES".lower():
				continue
			else:
				break
		elif is_win(vikings):
			print("You have lost! Good Luck next time!")
			again = input("Would you like to play again(YES or NO)")
			if again.lower() == "YES".lower():
				continue
			else:
				break

main()