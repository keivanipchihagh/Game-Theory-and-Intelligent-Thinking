'''
Implementation of Dooubly linked list
Created by: 		Keivan Ipchi Hagh
Creation data:		Monday, November 2, 2020

Purpose of this data structure is to have the minimum possible time complexity for each operation.
Modify the code for your own use.
'''

class Node:
	''' Node object contains a value, a pointers to next and a pointer to the previous node '''

	def __init__(self, value):
		''' Construction - Initializes the object variables '''
		self.next = self.prev = None
		self.value = value

class LinkedList:
	''' Doubly linked list '''

	def __init__(self):
		''' Construction - Initializes the object variables to default values '''
		self.head = self.tail = self.mid = None
		self.size = 0

	def push(self, value):
		''' Pushes a new Node to the head of the list - Time Complexity O(1) '''

		# Create a new Node and assign value
		new_node = Node(value)

		# Set a pointer from the new node to the head
		new_node.next = self.head

		# Increment the size by one
		self.size += 1

		if self.size == 1:
			# If only one Node exists, set middle and tail to the node
			self.mid = self.tail = new_node
		else:
			self.head.prev = new_node

			if self.size % 2 == 1:
				# Change middle node acoording to list's size
				self.mid = self.mid.prev

		# Set new node as the new head
		self.head = new_node

	def pop(self):
		''' Pops the head of the list - Throws exception if list is empty - Time Complexity O(1) '''

		if self.size == 0:
			# Raise error
			raise Exception('LinkedList is empty!')

		# Make a copy
		temp = self.head
		self.head = temp.next

		if self.head != None:
			self.head.prev = None

		# Decrement the size by one
		self.size -= 1

		if self.size % 2 == 0:
			# Adjust the middle node accordingly if there are even number of nodes in the list
			self.mid = self.mid.next

	def get_middle(self):
		''' Returns the value of the middle node in the list - Throws exception if list is empty - Time Complexity of O(1) '''

		if self.size == 0:
			# Raise error
			raise Exception('LinkedList is empty!')

		# Return value
		return self.mid.value

	def remove_middle(self):
		'''Removes the middle node of the list - Throws exception if list is empty - Time Complexity of O(1) '''

		if self.size == 0:
			# Raise error
			raise Exception('LinkedList is empty!')

		if self.size == 1:
			# Remove the only node in the list
			self.head = self.mid = None 
		else:

			# Disconnect the middle node
			self.mid.prev.next = self.mid.next

			# Gets tricky here!
			if self.size != 2:
				self.mid.next = self.mid.prev

			# Decrement size by one
			self.size -= 1

			if self.size % 2 == 0:
				# If even number of nodes are in the list, middle node is the one earlier pushed
				self.mid = self.mid.next
			else:
				self.mid = self.mid.prev


	def print(self):
		''' Prints the list values from head to tail - Time Complexity O(n) '''

		iterator = self.head
		while iterator != None:
			print(iterator.value, end = ' ')

			iterator = iterator.next	# Step
		print()

	def print_reversed(self):
		''' Prints the list values from tail to head - Time Complexity O(n) '''

		iterator = self.tail
		while iterator != None:
			print(iterator.value, end = ' ')

			iterator = iterator.prev 	# Step
		print()

	def print_first_half(self):
		''' Prints the first half of the list - Time Complexity O(n) '''

		iterator = self.head
		while iterator != mid:
			print(iterator.value, end = ' ')

			iterator = iterator.next	# Step
		print()

	def print_first_half(self):
		''' Prints the first half of the list - Time Complexity O(n) '''

		iterator = self.tail
		while iterator != mid:
			print(iterator.value, end = ' ')

		iterator = iterator.prev 		# Step
		print()