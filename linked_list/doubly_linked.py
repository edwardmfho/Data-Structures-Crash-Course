"""
Doubly Linked List Implementation
Prepared by edwardmfho

I need a refresher for data structure, therefore
I tried to implement each of the data structure 
using Python.

I still haven't finished implementing this 
doubly-linked list.


"""

# First we would need to create a Node object

class Node():
	def __init__(self, data = None):
		self.data = data
		self.prev = None # Compare to Singly-Linked List, we need to 
						 # include pointer to previous node
		self.next = None

	def get(self):
		return self.data

	def get_next(self):
		return self.next

	def get_prev(self):
		return self.prev

	def set_prev(self, new_prev):
		self.prev = new_prev

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
			prev_node = cur_node
			while cur_node.next != None:
				prev_node = cur_node
				cur_node = cur_node.next

			cur_node.next = new_node
			new_node.prev = prev_node

	def is_empty(self):
		return True if self.head == None else False

	def push_head(self, data):
		if self.is_empty():
			return 'Empty list'

		new_node = Node(data)
		cur_head = self.head

		self.head = new_node
		cur_head.set_prev(new_node)
		new_node.set_next(cur_head)


	def remove_tail(self): #To-Do
		if self.is_empty():
			return 'Empty list'

		cur_node = self.head
		prev_node = cur_node

		while cur_node.next != None:
			prev_node = cur_node
			cur_node = cur_node.next

		prev_node.set_next(None)


	def remove_value(self, target): #To-Do
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
