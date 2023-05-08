from numpy import array
MOVEMENT = {"north":array([0,1]),
			"south":array([0,-1]),
			"east":array([1,0]),
			"west":array([-1,0])}
class Area():
	def __init__(self):
		self.room_items = []
		self.usable_items = {}
		self.allowed_movements = []
		self.descriptions = {}