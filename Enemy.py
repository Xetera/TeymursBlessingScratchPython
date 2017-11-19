import random
import Items
import time
class Enemy:
	def __init__(self, level, health, name):
		# set variables when the monster is created
		# could add maxhealth here if we felt like adding mechanics to enemies
		self.health = health
		self.level = level
		self.name = name
		self.status = "Alive"

	def talk(self, quote):
		print("{} says: {}".format(self.name, quote))

	def attack(self, Timur):
		# calculates damage based on level
		damage = random.randrange(0 + self.level * 2, self.level * 4)
		Timur.takeDamage(damage, Timur)

	def takeDamage(self, damage_amount, Timur):
		self.health -= damage_amount

		print("{} took {} damage".format(self.name, damage_amount))
		print("{}'s HP: {}\n".format(self.name, self.health))
		
		if self.health < 0:
			time.sleep(0.5)
			self.die(Timur)


	def die(self, Timur):
		# reward experience based on the level of the monster
		self.status = "Dead"
		experience = 10 * self.level
		print("{} has been killed!".format(self.name))
		print("You have gained {} experience!".format(experience))
		if Timur.level > self.level:
			experience -= 10
		Timur.gainExperience(experience)

		if random.randrange(0, 100) < (100):
			self.itemDrop(Timur)
			# (100) is the % chance for stuff to drop normally, adjust accordingly

	def itemDrop(self, Timur):
		# not implementing actual items until game is working, just prints for now
		# print("length of all_items "+ str(len(Items.Collections.all_items)))
		choice = random.choice(list(Items.Collections.all_items))
		item = ""
		desc = ""
		for key, value in Items.Collections.all_items.items():
			if key == choice:
				item = key
				desc = value

		print("You found a new item:")
		print("Name: " + str(item))
		print("Description: {}\n".format(desc['Description']))
		# print("Stats: \n"))
		# TODO: implement a way to get stats shown up here properly
