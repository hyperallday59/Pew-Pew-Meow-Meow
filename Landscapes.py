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
		return "\n\n"+self.descriptions.get(key, "Invalid area setting - something broke")

	def special(self, key):
		if key == 'key':
			self.allowed_movements.append('south')

landscape = {}

entry = Area()
entry.area_items.append('key')
entry.usable_items['stick'] = "You use the stick to move the mound of dirt."
entry.allowed_movements.append('west')
entry.descriptions[((),())] = "Entry: Scattered dirt and a used stick."
landscape[(0,0)] = entry