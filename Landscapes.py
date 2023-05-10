from numpy import array
MOVEMENT = {"north":array([0,1]),
			"south":array([0,-1]),
			"east":array([1,0]),
			"west":array([-1,0])}
class Area():
	def __init__(self):
		self.area_items = []
		self.usable_items = {}
		self.allowed_movements = []
		self.descriptions = {}
	
	def get_item(self, hero):
		if self.area_items:
			item = input("What item would you like to grab? ").lower()
			if item in self.area_items:
				print(f"You pickup the {item}.")
				hero.inventory.append(item)
				self.area_items.remove(item)
			else:
				print(f"Couldn't find {item} in area.")
		else:
			print("There's nothing to pickup here!")
	
	def use_item(self, hero):
		if hero.inventory:
			print(f"Your inventory:\n{hero.inventory}")
			item = input("What item would you like to use? ").lower()
			if item in hero.inventory:
				if item in self.usable_items:
					print(self.useable_items[item])
					hero.inventory.remove(item)
					del self.usable_items[item]
					self.special(item)
				else:
					print(f"You can't use {item} here.")
			else:
				print(f"You don't have {item} in your inventory.")
		else:
			print("You don't have anything in your inventory to 'use'!")

	def move(self, hero):
		print(f"You can go in the following directions:\n{self.allowed_movements}")
		direction = input("Which direction would you like to run? ")
		if direction in MOVEMENT:
			if direction in self.allowed_movements:
				print(f"You move {direction}.")
				hero.position = direction
			else:
				print(f"You hit a wall of impenitrable bamboo, you can't move {direction} from here.")
		else:
			print(f"'{direction}' isn't a direction the hero can move")

	def description(self):
		key = tuple(self.area_items), tuple(self.usable_items)
		return "\n\n"+self.descriptions.get(key, "no" )

	def special(self, key):
		if key == 'key':
			self.allowed_movements.append('south')

landscape = {}

entry = Area()
entry.allowed_movements.append('south')
entry.descriptions[((),())] = "\nAfter months of training you finally return home to the Ninja Cat Village. You've been training to make your family proud and become the ninja you were always meant to be.\nBut... no one is in the village, it's as if it's been deserted.\nAfter searching the village for quite some time you find a letter. It's from your grandfather, the chief of Ninja Cat Village\ngrandson, the evil ninja cats have invaded our lands stealing our Ninja gear and enslaving us. If you find this we must have all already been taken! Your final test to become a true shinobi will be saving our people and reclaiming our Ninja gear! Luckily I located the Evil Ninja Cat Mansion located deep in the bamboo forest. It's...\nthe letter suddenly ends.\n\nDang it! you exclaim\nThey must have invaded the village while your grandfather was writing the letter.\n\nYou waste no time gathering what little supplies you have and embark for the bamboo forest. After a day or two of treacherous hiking you've finally reached it!\nThe entrance to the bamboo forest!\nMove south to start your journey"
landscape[(0,0)] = entry

Area_1 = Area()
Area_1.allowed_movements.append('north')
Area_1.allowed_movements.append('east')
Area_1.area_items.append('bamboo')
Area_1.descriptions[(('bamboo',),())] = "You've entered the Bamboo forest!\nYou notice tall walls of bamboo blocking you on in almost every direction. However you notice a small path headed east.\nYou also notice several stalks of sturdy cut bamboo lying around."
Area_1.descriptions[((),())] = "You've entered the Bamboo forest!\nYou notice tall walls of bamboo blocking you on in almost every direction. However you notice a small path headed east."
landscape[(0,-1)] = Area_1

Area_2 = Area()
Area_2.allowed_movements.append('west')
Area_2.allowed_movements.append('east')
Area_2.area_items.append('onion')
Area_2.descriptions[(('onion',),())] = "You head down the path and continue on for a while. Eventually you find a camp with a very old merchant. The trail runs through the camp and continues east.\nYou talk to the merchant and he offers you a reward if you can anwser his riddle\n\nYou cut me up, you chop me up, you dice me up and you cry over me. What am I?\n\nHINT: use the get command to anwser the riddle."
Area_2.descriptions[((),())] = "You've successfully beaten the old merhcants riddle!\nBeyond that the camp and trail remains the same"
landscape[(1,-1)] = Area_2

Area_3 = Area()
Area_3.allowed_movements.append('west')
Area_3.allowed_movements.append('south')
Area_3.usable_items['bamboo'] = "After sneaking up on the enemy you use your bamboo like a baseball bat and crack it acrost the back of his head.\nwith one blow the enemy has been defeated"
Area_3.area_items.append('sword')
Area_3.descriptions[(('sword',),('bamboo',))] = "Not long after meating the merchant, you stumble acrost one of the evil ninja cat camps.\nYou notice one of the enemies on the outskirts of the camp is playing with one of your clans sacred swords.\nYou might be able to sneak attack him from behind!"

Area_3.descriptions[((),())] = "You've successfully beaten the old merhcants riddle!\nBeyond that the camp and trail remains the same"
landscape[(2,-1)] = Area_2
