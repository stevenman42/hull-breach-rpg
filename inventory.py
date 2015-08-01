class Inventory(object):
	def __init__(self, stuff=[]):
		self.items = []
		for i in self.items:
			self.items.append(i)
			
	def add_item(self, item):
		self.items.append(item)

	def remove_item(self, item):
		self.items.remove(item)