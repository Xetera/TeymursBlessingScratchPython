import random

class Enemy:
	def __init__(self, level, health, name):
		# set variables when the monster is created
		# could add maxhealth here if we felt like adding mechanics to enemies
		self.health = health
		self.level = level
		self.name = name

	def talk(self, quote):
		print("{} says: {}".format(self.name, quote))

	def attack(self, Timur):
		# calculates damage based on level
		damage = random.randrange(0 + self.level *2, self.level *4)
		Timur.takeDamage(damage)

	def takeDamage(self, damage_amount):
		if self.health - damage_amount < 0:
			self.die()
		self.health -= damage_amount

	def die(self, name, Timur):
		# reward experience based on the level of the monster
		experience = 10 * self.level
		print("{} has been killed!".format())
		if Timur.level > self.level:
			experience -= 10
		Timur.gainExperience(experience)

		if random.randrange(0, 100) < (20):
			self.itemDrop()
			# 20% chance for stuff to drop

	def itemDrop(self, Timur):
		# not implementing actual items until game is working, just prints for now
		choice = random.randrange(len(Items.Collections.all_items))
		item = Items.Collections[choice]
		print("You found a new item:")
		print("Name: " + item)
		print("Description: " + item['Description'])
		print("Stats: " + item['Stats'])
