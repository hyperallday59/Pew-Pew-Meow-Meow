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
					print(self.usable_items[item])
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
		if key == 'secret':
			self.allowed_movements.append('south')
		if key == 'horn':
			self.allowed_movements.append('east')

landscape = {}

area = Area()
area.allowed_movements.append('south')
area.descriptions[((),())] = "\nAfter months of training you finally return home to the Ninja Cat Village. You've been training to make your family proud and become the ninja you were always meant to be.\nBut... no one is in the village, it's as if it's been deserted.\nAfter searching the village for quite some time you find a letter. It's from your grandfather, the chief of Ninja Cat Village\ngrandson, the evil ninja cats have invaded our lands stealing our Ninja gear and enslaving us. If you find this we must have all already been taken! Your final test to become a true shinobi will be saving our people and reclaiming our Ninja gear! Luckily I located the Evil Ninja Cat Mansion located deep in the bamboo forest. It's...\nthe letter suddenly ends.\n\nDang it! you exclaim\nThey must have invaded the village while your grandfather was writing the letter.\n\nYou waste no time gathering what little supplies you have and embark for the bamboo forest. After a day or two of treacherous hiking you've finally reached it!\nThe entrance to the bamboo forest!\nMove south to start your journey"
landscape[(0,0)] = area

area = Area()
area.allowed_movements.append('north')
area.allowed_movements.append('east')
area.area_items.append('bamboo')
area.descriptions[(('bamboo',),())] = "You've entered the Bamboo forest!\nYou notice tall walls of bamboo blocking you on in almost every direction. However you notice a small path headed east.\nYou also notice several stalks of sturdy cut bamboo lying around."
area.descriptions[((),())] = "You've entered the Bamboo forest!\nYou notice tall walls of bamboo blocking you in almost every direction. However you notice a small path headed east."
landscape[(0,-1)] = area

area = Area()
area.allowed_movements.append('west')
area.allowed_movements.append('east')
area.area_items.append('onion')
area.descriptions[(('onion',),())] = "You head down the path and continue on for a while. Eventually you find a camp with a very old merchant. The trail runs through the camp and continues east.\nYou talk to the merchant and he offers you a reward if you can anwser his riddle\n\nYou cut me up, you chop me up, you dice me up and you cry over me. What am I?\n\nHINT: use the get command to anwser the riddle."
area.descriptions[((),())] = "You've successfully beaten the old merhcants riddle!\nAs he promised he gives you a reward, an onion\nBeyond that the camp remains the same and the trail continues east."
landscape[(1,-1)] = area

area = Area()
area.allowed_movements.append('west')
area.allowed_movements.append('south')
area.usable_items['bamboo'] = "After sneaking up on the enemy you use your bamboo like a baseball bat and crack it acrost the back of his head.\nwith one blow the enemy has been defeated"
area.area_items.append('sword')
area.descriptions[(('sword',),('bamboo',))] = "Not long after meating the merchant, you stumble acrost one of the evil ninja cat camps.\nYou notice one of the enemies on the outskirts of the camp is playing with one of your clans sacred swords.\nYou might be able to sneak attack him from behind!"
area.descriptions[(('sword',),())] = "The enemy lies at your feet, and the sword he was using is next to him. The trail continues south."
area.descriptions[((),())] = "The enemy lies at your feet. The trail continues south."
landscape[(2,-1)] = area

area = Area()
area.allowed_movements.append('south')
area.allowed_movements.append('north')
area.area_items.append('secret')
area.descriptions[(('secret',),())] = "After running south you reach a clearing. The trail continues through the clearing heading south.\nIn the clearing there is a mysterious box that has a riddle enscribed on it, you try to open it.\nIt won't budge. The riddle reads\n\nI'm something you can hold, but you can't touch, You can whisper me softly, but I won't say much. I'm kept in a place where no one can find, And locked in a vault inside your mind. Some people keep me safe, and others let me out, Some people share me freely, while others tightly pout. I can make you feel powerful, or make you feel weak, I can be hidden for ages, or revealed in a peek.\n\nMaybe if you can anwser the riddle the box will open.\nHINT: use the get command to anwser the riddle."
area.descriptions[((),())] = "You've solved the riddle. The boxes lid flies open and a mysterious power flows into you, you hear a voice whisper\n'the power of a secret'\n The empty box is in front of you. The clearing remains the same and the trail continues south."
landscape[(2,-2)] = area

area = Area()
area.usable_items['secret'] = "The bamboo accepts your secret and lets you move forward"
area.allowed_movements.append('north')
area.descriptions[((),('secret',))] = "Suddenly as your traveling along the path it ends, A wall of bamboo has blocked the path. You find a sign nearby. Inscribed on the sign is the message 'tell me your hiddden truth'."
area.descriptions[((),())] = "You told the bamboo your powerfull secret. It will now let you continue down the path heading south."
landscape[(2,-3)] = area

area = Area()
area.allowed_movements.append('east')
area.allowed_movements.append('west')
area.allowed_movements.append('north')
area.descriptions[((),())] = "After following the path for some time you reach a fork in the path. One way heads east, and the other heads west."
landscape[(2,-4)] = area

area = Area()
area.allowed_movements.append('west')
area.area_items.append('key')
area.usable_items['horn'] = "You blow the horn with all your might. At first it seems as if nothing has happened.\nSuddenly you hear a big bang and the water fall parts revealing a secret passage"
area.descriptions[(('key',),('horn',))] = "After heading east you reach a shallow pool of water. The pool is surrounded by bamboo and has a water fall flowing into it.\nYou notice something shiny at the bottom of the pool."
area.descriptions[((),('horn',))] = "You found a key at the bottom of the pool, you wonder what it goes to. the pool and water fall remain the same.\nThe water fall has a suspicious glint"
area.descriptions[((),())] = "The shallow pool of water remains as beautiful as ever. You can either head back the way you came or down the secret passage."
landscape[(3,-4)] = area

area = Area()
area.allowed_movements.append('east')
area.allowed_movements.append('west')
area.area_items.append('horn')
area.usable_items['key'] = "You've opened the old chest and revealed an old battle horn."
area.descriptions[(('horn',),('key',))] = "After heaing west you find a mysterious chest\nMaybe you can find something to open it\nThe path continues west"
area.descriptions[(('horn',),())] = "The chest in the middle of the path is now open and a battle horn rests inside\n the path continues west"
area.descriptions[((),())] = "The empty chest sits in the middle of the path\nThe path continues west"
landscape[(1,-4)] = area

area = Area()