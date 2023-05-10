import random
import pickle
from numpy import array
from Landscapes import landscape, MOVEMENT
ACTIONS = ("quit", "save", "load", "get", "use", "move")

class Hero():
	def __init__(self):
		self.__position = (0, 0)
		self.inventory = []
		self.name = input("What is your name\nOh Great Warrior?\n").title()
		
	@property
	def position(self):
		return tuple(self.__position)
		
	@position.setter
	def position(self,new):
		self.__position += MOVEMENT[new]

def valid_input(prompt = "What would you like to do? "):
	print("\t--Options--")
	response = None
	while response not in ACTIONS:
		print(f"Actions:\n{ACTIONS}")
		response = input(prompt).lower()
	return response

def save():
	'''save the player object and rooms dictionary to a file'''
	with open('game.dat','wb') as f:
		pickle.dump(Hero,f)
		pickle.dump(landscape,f)
	print("Game saved!")

def load():
	'''load the hero object and rooms dictionary from a file'''
	#using global variables to reduce size
	global Hero
	global Landscape
	try:
		with open("game.dat",'rb') as f:
			Hero = pickle.load(f)
			Landscape = pickle.load(f)
		print("Game loaded!")
	except FileNotFoundError:
		print("Game file not found!")

hero = Hero()
def main(hero):
	choice = None
	while choice != "quit":
		#unpack current room variables
		room = landscape.get(hero.position, "Invalid room setting - something broke")
		print(room.description())
		choice = valid_input()
		if choice == "quit":
			print("Thanks for playing!")
		elif choice == "save":
			save()
		elif choice == "load":
			load()
		elif choice == "get":
			room.get_item(hero)
		elif choice == "use":
			room.use_item(hero)
		elif choice == "move":
			room.move(hero)

if __name__ == "__main__":
	main(hero)