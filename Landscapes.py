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
			item = input("What item would you like to 'get'? ").lower()
			if item in self.area_items:
				print(f"You pickup the {item}.")
				hero.inventory.append(item)
				self.area_items.remove(item)
			else:
				print(f"Couldn't find {item} in room.")
		else:
			print("There's nothing to pickup here!")
