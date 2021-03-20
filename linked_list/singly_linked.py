# First we would need to create a Node object

class Node():
	def __init__(self, data = None):
		self.data = data
		self.next = None

	def get(self):
		return self.data

	def get_next(self):
		return self.next

	def set_next(self, new_next):
		self.next = new_next

# Then we would create a linkedlist object

class LinkedList():
	def __init__(self):
		self.head = None

	def push(self, data):
		if self.head == None:
			new_node = Node(data)
			self.head = new_node

		else:
			new_node = Node(data)
			cur_node = self.head

			while cur_node.next != None:
				cur_node = cur_node.next

			cur_node.next = new_node

	def is_empty(self):
		return True if self.head == None else False

	def remove_tail(self):
		if self.is_empty():
			return 'Empty list'

		cur_node = self.head
		prev_node = cur_node

		while cur_node.next != None:
			prev_node = cur_node
			cur_node = cur_node.next

		prev_node.set_next(None)


	def remove_value(self, target):
		if self.is_empty():
			return 'Empty list'
		cur_node = self.head
		prev_node = cur_node

		while cur_node.data != target and cur_node.next != None:
			prev_node = cur_node
			cur_node = cur_node.next			

		prev_node.set_next(cur_node.next)


	def get_all(self):
		if self.is_empty():
			return 'Empty list'
		linkedlist_items = []

		if self.head != None: #If list is not empty
			cur_node = self.head
			linkedlist_items.append(cur_node.data)
			while cur_node.next != None:
				cur_node = cur_node.next
				linkedlist_items.append(cur_node.data)
		return linkedlist_items
