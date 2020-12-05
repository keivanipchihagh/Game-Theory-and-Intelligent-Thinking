'''
Implementation of Dooubly linked list
Created by: 		Keivan Ipchi Hagh
Creation data:		Monday, November 2, 2020
GitHub:				https://github.com/keivanipchihagh

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
	''' 
	~ Doubly linked list (Python 3 edition) ~

	functions:
	- push 							O(1)	Return: -			Parameters: Value
	- pop 							O(1)	Return: Node 		Parameters: -
	- get_middle 					O(1)	Return: Node 		Parameters: -
	- remove_middle					O(1)	Return: - 			Parameters: -
	- shift_left					O(1)	Return: -			Parameters: -
	- shift_right					O(1)	Return: -			Parameters: -
	- get_list						O(n)	Return: List 		Parameters: reversed
	- exists 						O(n)	Return: Boolean 	Parameters: Value
	- push_all						O(n)	Return: -			Parameters: List
	- print 						O(n)	Return: -			Parameters: new_line, reversed
	'''

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

	def push_all(self, ls):
		''' Pusges an iterable into the linkedlist '''

		ls = list(ls)
		for item in ls:
			self.push(item)

	def pop(self, return_popped = True):
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

		if return_popped == True:
			# Returns popped item if needed
			return temp	# Return poped item

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

			# If even number of nodes are in the list, middle node is the one earlier pushed
			self.mid = self.mid.next if (self.size % 2 == 0) else self.mid.prev			

	def exists(self, value):
		''' Checks whether the given value exists in the list or not '''

		iterator = self.head
		while iterator != None:
			if iterator.value == value:
				return True

			iterator = iterator.next	# Step
		return False

	def print(self, new_line = True, reversed = False):
		''' Prints the list values from head to tail - Time Complexity O(n) '''

		iterator = self.tail if (reversed == True) else self.head		

		while iterator != None:
			print(iterator.value, end = ' ')
			iterator = iterator.prev if (reversed == True) else iterator.next	# Step

		if new_line == True:
			# Go to new line if needed
			print()

	def shift_left(self):
		''' Moves the head to the tail '''

		if self.size > 1:

			# Get the current head
			temp = self.pop()

			temp.next = None
			self.tail.next = temp
			temp.prev = self.tail

			# Set as tail
			self.tail = temp

	def shift_right(self):
		''' Moves the tail to the head '''

		if self.size > 1:

			# pop the current tail
			temp = self.tail

			self.tail = self.tail.prev
			self.tail.next = None
			
			temp.prev = None
			self.head.prev = temp
			temp.next = self.head

			# Set as head
			self.head = temp

	def get_list(self, reversed = False):
		''' Returns the list of all node values '''

		iterator = self.tail if (reversed == True) else self.head

		ls = []

		while iterator != None:
			ls.append(iterator.value)			
			iterator = iterator.prev if (reversed == True) else iterator.next	# Step

		return ls	

# Show case
ll = LinkedList()								# Initialize

ll.push_all([1, 2, 3, 4, 5, 6])					# Push an iterable

ll.push(7)										# Push a value

ll.print(new_line = True, reversed = False)		# Print

print(ll.exists(8))								# Check exists

ll.shift_right()								# Shift right

ll.shift_left()									# Shift left

ll.print(reversed = True)						# Print reversed

print(ll.get_list(reversed = False))			# Convert to list