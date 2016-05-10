class Inventory(object):
	def __init__(self, stuff=[]):
		self.items = []
		self.equips = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
		# 1 equip slots:
		# 2 head
		# 3 torso/arms
		# 4 hands
		# 5 fingers
		# 6 weapon (stuff you actually hold)
		# 7 legs
		# 8 feet
		for i in stuff:
			self.items.append(i)
			
	def add_item(self, item):
		self.items.append(item)

	def remove_item(self, item):
		self.items.remove(item)

	def equip_item(self, item, slot):
		if item not in self.items:
			return False
		else:
			if self.equips[slot] != 0:
				return False
			else:
				self.equips[slot] = item
				return "You equip the " + item.description + " " + item.name


	def unequip_item(self, item, slot):
		if item not in self.items:
			return False