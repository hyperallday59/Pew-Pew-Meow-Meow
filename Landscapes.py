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
		if key == 'invisibility':
			self.allowed_movements.append('west')
		if key == 'rope':
			self.allowed_movements.append('west')
		if key == 'lock pick':
			self.allowed_movements.append('west')
		if key == 'silver key':
			self.allowed_movements.append('south')
		if key == 'bow and arrow':
			self.allowed_movements.append('east')
		if key == 'sword':
			self.allowed_movements.append('east')
		if key == 'shield':
			self.allowed_movements.append('south')
		if key == 'spear':
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
Area_1.descriptions[((),())] = "You've entered the Bamboo forest!\nYou notice tall walls of bamboo blocking you in almost every direction. However you notice a small path headed east."
landscape[(0,-1)] = Area_1

Area_2 = Area()
Area_2.allowed_movements.append('west')
Area_2.allowed_movements.append('east')
Area_2.area_items.append('onion')
Area_2.descriptions[(('onion',),())] = "You head down the path and continue on for a while. Eventually you find a camp with a very old merchant. The trail runs through the camp and continues east.\nYou talk to the merchant and he offers you a reward if you can anwser his riddle\n\nYou cut me up, you chop me up, you dice me up and you cry over me. What am I?\n\nHINT: use the get command to anwser the riddle."
Area_2.descriptions[((),())] = "You've successfully beaten the old merhcants riddle!\nAs he promised he gives you a reward, an onion\nBeyond that the camp remains the same and the trail continues east."
landscape[(1,-1)] = Area_2

Area_3 = Area()
Area_3.allowed_movements.append('west')
Area_3.allowed_movements.append('south')
Area_3.usable_items['bamboo'] = "After sneaking up on the enemy you use your bamboo like a baseball bat and crack it acrost the back of his head.\nwith one blow the enemy has been defeated"
Area_3.area_items.append('sword')
Area_3.descriptions[(('sword',),('bamboo',))] = "Not long after meating the merchant, you stumble acrost one of the evil ninja cat camps.\nYou notice one of the enemies on the outskirts of the camp is playing with one of your clans sacred swords.\nYou might be able to sneak attack him from behind!"
Area_3.descriptions[(('sword',),())] = "The enemy lies at your feet, and the sword he was using is next to him. The trail continues south."
Area_3.descriptions[((),())] = "The enemy lies at your feet. The trail continues south."
landscape[(2,-1)] = Area_3

Area_4 = Area()
Area_4.allowed_movements.append('south')
Area_4.allowed_movements.append('north')
Area_4.area_items.append('secret')
Area_4.descriptions[(('secret',),())] = "After running south you reach a clearing. The trail continues through the clearing heading south.\nIn the clearing there is a mysterious box that has a riddle enscribed on it, you try to open it.\nIt won't budge. The riddle reads\n\nI'm something you can hold, but you can't touch, You can whisper me softly, but I won't say much. I'm kept in a place where no one can find, And locked in a vault inside your mind. Some people keep me safe, and others let me out, Some people share me freely, while others tightly pout. I can make you feel powerful, or make you feel weak, I can be hidden for ages, or revealed in a peek.\n\nMaybe if you can anwser the riddle the box will open.\nHINT: use the get command to anwser the riddle."
Area_4.descriptions[((),())] = "You've solved the riddle. The boxes lid flies open and a mysterious power flows into you, you hear a voice whisper\n'the power of a secret'\n The empty box is in front of you. The clearing remains the same and the trail continues south."
landscape[(2,-2)] = Area_4

Area_5 = Area()
Area_5.usable_items['secret'] = "The bamboo accepts your secret and lets you move forward"
Area_5.allowed_movements.append('north')
Area_5.descriptions[((),('secret',))] = "Suddenly as your traveling along the path it ends, A wall of bamboo has blocked the path. You find a sign nearby. Inscribed on the sign is the message 'tell me your hiddden truth'."
Area_5.descriptions[((),())] = "You told the bamboo your powerfull secret. It will now let you continue down the path heading south."
landscape[(2,-3)] = Area_5

Area_6 = Area()
Area_6.allowed_movements.append('east')
Area_6.allowed_movements.append('west')
Area_6.allowed_movements.append('north')
Area_6.descriptions[((),())] = "After following the path for some time you reach a fork in the path. One way heads east, and the other heads west."
landscape[(2,-4)] = Area_6

Area_7 = Area()
Area_7.allowed_movements.append('west')
Area_7.area_items.append('key')
Area_7.usable_items['horn'] = "You blow the horn with all your might. At first it seems as if nothing has happened.\nSuddenly you hear a big bang and the water fall parts revealing a secret passage"
Area_7.descriptions[(('key',),('horn',))] = "After heading east you reach a shallow pool of water. The pool is surrounded by bamboo and has a water fall flowing into it.\nYou notice something shiny at the bottom of the pool.\nIt looks like a key"
Area_7.descriptions[((),('horn',))] = "You found a key at the bottom of the pool, you wonder what it goes to. the pool and water fall remain the same.\nThe water fall has a suspicious glint, there might be a secret passage"
Area_7.descriptions[((),())] = "The shallow pool of water remains as beautiful as ever. You can either head back the way you came or down the secret passage."
landscape[(3,-4)] = Area_7

Area_8 = Area()
Area_8.allowed_movements.append('east')
Area_8.allowed_movements.append('west')
Area_8.area_items.append('horn')
Area_8.usable_items['key'] = "You've opened the old chest and revealed an old battle horn."
Area_8.descriptions[(('horn',),('key',))] = "After heaing west you find a mysterious chest\nMaybe you can find something to open it\nThe path continues west"
Area_8.descriptions[(('horn',),())] = "The chest in the middle of the path is now open and a horn rests inside\n the path continues west"
Area_8.descriptions[((),())] = "The empty chest sits in the middle of the path\nThe path continues west"
landscape[(1,-4)] = Area_8

Area_9 = Area()
Area_9.allowed_movements.append('east')
Area_9.usable_items['invisibility'] = "you use the invisibility the dragon gifted you. Using this ability you easily sneak past and take out the enemies.\nYou can now continue down the path."
Area_9.descriptions[((),('invisibility',))] = "you come to a sudden halt as you head down the path. You notice two enemy Cat Ninjas in front of you.\nLuckily they haven't noticed you. There must be a way past them"
Area_9.descriptions[((),())] = "You've successfully snuck past and defeated the enemies. You can continue down the path!"
landscape[(0,-4)] = Area_9

Area_10 = Area()
Area_10.allowed_movements.append('west')
Area_10.usable_items['onion'] = "you give the dragon an onion"
Area_10.area_items.append('invisibility')
Area_10.descriptions[(('invisibility',),('onion',))] ="You enter a large cavern filled with gold, the only exit being the one you came through, At the center sits a mighty dragon. The dragon speaks\n\nYou who has entered my cave, bring me my favorite vegatable and I'll lend you my power"
Area_10.descriptions[(('invisibility',),())] = "Thank you young one, the dragon booms, I'll lend you my power\nThe dragon gifts you the power of invisibility\nHINT: you need to grab the power up"
Area_10.descriptions[((),())] = "You've claimed the power of invisibility\nThe dragon is happily munching on his onion\nThe only exit is the entrance to the cave"
landscape[(4,-4)] = Area_10

Area_11 = Area()
Area_11.allowed_movements.append('west')
Area_11.allowed_movements.append('east')
Area_11.area_items.append('shield')
Area_11.descriptions[(('shield',),())] = "While heading down the path you spot one of the sacred chests locked by a magical riddle from the Ninja cat village, They must have dropped it on the trail.\nThe riddle on the chest reads\nI'm by nature solitary, scarred by spear and wounded by sword, weary of battle. I frequently see the face of war, and fight hateful enemies; yet I hold no hope of help being brought to me in the battle, before I'm eventually done to death. What am I\n Solve the riddle and the box will open\nThe path continues west"
Area_11.descriptions[((),())] = "Congradulations you've solved the riddle!\nThe path continues west"
landscape[(-1,-4)] = Area_11

Area_12 = Area()
Area_12.allowed_movements.append('west')
Area_12.allowed_movements.append('east')
Area_12.area_items.append('rope')
Area_12.descriptions[(('rope',),())] = "While traveling down the path you run into a run down cart. You search the cart and find some old rope\nThe path continues west"
Area_12.descriptions[((),())] = "You've grabed the old rope from the cart, the cart is now empty\nThe path continues west"
landscape[(-2,-4)] = Area_12

Area_13 = Area()
Area_13.allowed_movements.append('east')
Area_13.usable_items['rope'] = "you use the old rope to climb down the clif"
Area_13.descriptions[((),('rope',))] = "The path suddenly stops, a cliff lies  before you, but you see that the path continues at the bottom.\nThere must be a way to get down"
Area_13.descriptions[((),())] = "You tie the rope to a nearby rock and use it to traverse the cliff, you can now continue down the path"
landscape[(-3,-4)] = Area_13

Area_14 = Area()
Area_14.allowed_movements.append('west')
Area_14.allowed_movements.append('east')
Area_14.allowed_movements.append('south')
Area_14.area_items.append('bow and arrow')
Area_14.descriptions[(('bow and arrow',),())] = "You reach the bottom of the cliff and continued down the path. After walking for some time you reach another cross road, one direction heading west, and the other heading south.\nYou notice that near the cross roads there is an old bow and arrow"
Area_14.descriptions[((),())] = "You reach the bottom of the cliff and continued down the path. After walking for some time you reach another cross road, one direction heading west, and the other heading south.\n There are no signs of any other loot around the cross roads"
landscape[(-4,-4)] = Area_14

Area_15 = Area()
Area_15.allowed_movements.append('east')
Area_15.usable_items['lock pick'] = "you use the lock pick to unlock the iron doors"
Area_15.descriptions[((),('lock pick',))] = "You continue to travel east and find that the path leads to a massive cave. The cave entrance is gaurded by a massive locked iron door.\nIf only there was some way to unlock it"
Area_15.descriptions[((),())] = "the iron doors clamber open, letting you continue on into the cave."
landscape[(-5,-4)] = Area_15

Area_16 = Area()
Area_16.allowed_movements.append('north')
Area_16.allowed_movements.append('east')
Area_16.area_items.append('lock pick')
Area_16.descriptions[(('lock pick',),())] ="While heading south you meet a suspicious character,\nHello there stranger, anwser my riddle and I'll give you a prize!\nI am the key that fits no lock, yet I open what is closed and blocked. What am I?\nThe path turns and continues east"
Area_16.descriptions[((),())] = "Good job stranger take this lock pick\nWith that the stranger has lost interest in you and continued on his way.\nThe path turns and continues east"
landscape[(-4,-5)] = Area_16

Area_17 = Area()
Area_17.allowed_movements.append('west')
Area_17.usable_items['silver key'] = "You use the silver key to unlock the back door of the enemy ninja cat's castle"
Area_17.descriptions[((),('silver key',))] = "You've finally reached the enemy ninja cat's castle. But the entrance to the castle is very heavily guarded.\nyou decide to look for a secret entrance. After hours of searching you finally find a secret back door\nBut, the door is locked by a silver padlock blocking your entrance\nMove west to return to the path"
Area_17.descriptions[((),())] = "The padlock on the door falls to the ground granting you entrance to the castle.\nMove south the enter the castle, Move west to return to the path"
landscape[(-3,-5)] = Area_17

Area_18 = Area()
Area_18.allowed_movements.append('east')
Area_18.allowed_movements.append('north')
Area_18.area_items.append('spear')
Area_18.descriptions[(('spear',),())] = "You reach the back of the cave, Theres another chest in front of you locked by a magical riddle\nTo the north you notice something glowing in cavity in the wall\n The riddle on the box reads\nI'm made of wood or sometimes steel, My point is sharp, my aim is real. I'm hurled through air with strength and might, And can bring down a beast with just one strike. What am I?"
Area_18.descriptions[((),())] = "The box opens and reveals a very powerful ancient spear. You gladly take the spear.\nTo the north you notice something glowing in cavity in the wall"
landscape[(-6,-4)] = Area_18

Area_19 = Area()
Area_19.allowed_movements.append('south')
Area_19.area_items.append('silver key')
Area_19.descriptions[(('silver key',),())] = "As you approach the cavity you find the skeleton of a ninja cat imprisoned in the cave. He clutches a silver key in his right hand\nMove south to walk back to the chest"
Area_19.descriptions[((),())] = "As you approach the cavity you find the skeleton of a ninja cat imprisoned in the cave.\nMove south to head back to the chest"
landscape[(-6,-3)] = Area_19

Area_20 = Area()
Area_20.allowed_movements.append('north')
Area_20.usable_items['bow and arrow'] = "You shoot an arrow at the shinobi captain and hit him directly in the knee, he falls to the ground, getting a bit full of yourself you approach the enemy\nsuddenly the enemy stands up and slashes directly at your head\nYou backflip and barely dodge the slash\n you draw your bow mid flip and shooting him through the eye\ndefeating the enemy"
Area_20.descriptions[((),('bow and arrow',))] = "You sneak through the castle using your shinobi skill. You finally reach the prison part of the castle.\nGuarding the door to the prison is one of the evil shinobi generals. The general is carrying several knifes, and no shield\n"
Area_20.descriptions[((),())] = "Your shinobi training has finally come in clutch. You have defeated the enemy and can now procede through the door"
landscape[(-3,-6)] = Area_20

Area_21 = Area()
Area_21.allowed_movements.append('west')
Area_21.usable_items['sword'] = "You draw your sword and accept the generals challenge.\nYou fight for what seems like ages, you and the general are equally matched.\n You notice a pool of water on the floor nearby and begin to push the  enemy towards it. Finally you go for a jab and he slips on the floor, landing you the victory"
Area_21.descriptions[((),('sword',))] = "You rushed through the door, and much to your dismay instead of seeing your friends your greeted with yet another shinobi general.\nThe general challenges you to a one on one sword duel"
Area_21.descriptions[((),())] = "The general lies lifeless on the floor. The dungeon your currently in has no prisoners, every cell is empty.\nYou find another door leading deeper east into the prison"
landscape[(-2,-6)] = Area_21

Area_22 = Area()
Area_22.allowed_movements.append('west')
Area_22.usable_items['shield'] = "You crouch as low as you can and use your shield to block as many arrows as you can"
Area_22.descriptions[((),('shield',))] =" Having defeated two generals you head through the door in the prison. It leads to a dark hallway that you begin to get traverse.\nSuddenly you step on a pressure plate and arows shoot towards you from the end of the hallway.\nYou barely dodge.\nThere must be some way to get Pst the arrows."
Area_22.descriptions[((),())] = "You make it through the hallway unscathed.\nSadly your shield did not\nAt the end of the hallway is a door heading south."
landscape[(-1,-6)] = Area_22

Area_23 = Area()
Area_23.allowed_movements.append('north')
Area_23.usable_items['spear'] = "You use the spear and barely manage to fend him off. The two of you begin to engage in an epic battle\nBut, the general has the upper hand, an you are slowly losing\nsuddenly you hear your grandpas voice\nYou've got it kiddo\n Pride and confidence begin to fill you with new found power\nYou put your everything in one final attack.\n You thrust the spear through the generals stomach and win the fight"
Area_23.descriptions[((),('spear',))] ="You enter the more secured area of the prison, at the very far side of this area you see people in cells\nSo you've come a loud voice booms\nYou were so distracted with finding your family that you completely missed the prison general\nHe throws 3 kunei at you all of which you barely dodge. He begins to rush you, defend yourself!"
Area_23.descriptions[((),())] = "You've won the fight and beaten all of your enemies, all thats left is to free your people\nMove South"
landscape[(-1,-7)] = Area_23

Area_24 = Area()
Area_24.descriptions[((),())] = "You free your people and storm the castle using the ninja gear you've reclaimed\nCongradulations\nYou've beat the Game!"
landscape[(-1,-8)] = Area_24
#final save