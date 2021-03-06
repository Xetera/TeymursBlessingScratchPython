import time
import Story
import Enemy


class Game:
	def __init__(self): # things that happen when you're starting the game
		self.game_name = "Teymur\'s Blessing"
		print(Story.INTRO)
		# testing encounterEnemy

	def losegame(self, Timur): # losing the game
		print("You lost the game")
		print("You lost the game at: " + Timur.level)
		print("Your final stats:")
		for key, value in Timur.stats.items(): # get me everything inside Timur's stats
			print("{}: {}".format(key, value)) # [Strength] = its value (10 or whatever)

	def encounterEnemy(self, level, health, name):
		print("You have encountered a {}!".format(name))
		print("Level: {}\nHealth: {}\n".format(level,health))
		return Enemy.Enemy(level, health, name)
		# create a new Enemy with given level, health and name. Returns it to set to a variable

	def listenForAttack(Timur, target): # target must be passed as obj
		while target.status != "Dead":
			while True: # this lets us keep asking for an attack until we get a valid input
				# print out every move that Timur has
				attack_map = {}

				for move, value in Timur.moves.items():
					#  attack_map[i] = move
					# enumerate allows us to assign numbers to moves
					# this lets us just type the number of the attack without
					# having to type out the whole name every time
					print("{}\nDamage: {}\n".format(move.title(), value['Damage']))
					# i (Autism)
					# Damage: i['Damage'] (10)
				selection = input("Select an attack:\n")
				if selection not in Timur.moves:
					print("That's not a valid move.")
					continue # go back to the beginning of the loop


				Timur.executeAttack(Timur.moves[selection.lower()], target)
				# attacks are stored in lowercase to in case someone enters
				# 'aUtiSm' we still want it to work
				break # break out of the loop

	def playersTurn(self):
		pass
