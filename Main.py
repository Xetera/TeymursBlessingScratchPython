import random # random is a module that we have to import to get random numbers

from Game import Game # import the class 'Game' from the file 'Game.py'

import Items # Import the file 'Items.py'


class Teymur:
	def __init__(self): # values that are set when Teymur is defined (game starts)
		# initiate empty dictionary that we will later add things to
		self.stats = {}
		self.moves = {}
		self.inventory = {}

		# fill up the dictionary 'stats' with stats
		self.stats['Strength'] = 8
		self.stats['Dexterity'] = 3
		self.stats['Intelligence'] = 7
		self.stats['Luck'] = 1
		self.stats['Stamina'] = 2
		self.stats['Vitality'] = 4
		self.level = 1

		# useful for calculating levels
		self.maxexperience = 50
		self.experience = 0

		# health
		self.maxhealth = 10 + (2 * self.stats['Stamina'])
		self.health = self.maxhealth

		# This part creates new moves, gives name, description and damage
		# this is run on __init__ because it's the default moves
		self.newmove("Dab", "Dabs on them hates", 1)
		self.newmove("Monkey Yell", "Yells incredibly monkily", 2)
		self.newmove("Seizure", "Has an intense seizure", 4)
		self.newmove("Anime", "Passes one turn to watch anime", 0)

	def increaseStats(Str=0, Dex=0, Int=0, Luck=0, Stm=0, Vit=0):
		# these values are all 0 unless you state what they are
		self.stats['Strength'] += Str
		self.stats['Dexterity'] += Dex
		self.stats['Intelligence'] += Int
		self.stats['Luck'] += Luck
		self.stats['Stamina'] += Stm
		self.stats['Vitality'] += Vit

	def newmove(self, nameofmove, description, damage):
		self.moves[nameofmove] = {} # make a new dictionary inside of dictionary
		self.moves[nameofmove]['Description'] = description # set description
		self.moves[nameofmove]['Damage'] = damage # set damage

	def takeDamage(damage):
		if self.health - damage < 0: # if your heath drops under 0, die
			losegame()
		self.health - damage # subtract health equal to damage

	def getStats(self):
		# will need this later to display stats
		pass

	def executeAttack(self, move, target, special=False):
		# move must be passed as an obj, not name
		self.dealDamage(name, target)

	def dealDamage(self, selected_move, enemy): # deal damage to enemy
		move = self.moves[selected_move]
		damage_amount = (self.stats['Strength'] * self.level) + 1
		enemy.takeDamage(damage_amount)

	def gainExperience(self, xp_amount): # I mean, makes sense
		# should we be using a set xp here or gain some based on level %?
		self.experience += xp_amount
		# if our experience is greater or equal to max xp, level up
		if self.experience >= self.maxexperience:
			# new experience amount is how much we went over the old amount
			self.experience = self.experience - self.maxexperience
			self.levelup()
	def levelup(self):
		# I'm not sure which stats should level up how so I'm making them all 2
		self.increaseStats()



class Zone:
	pass

game = Game()
