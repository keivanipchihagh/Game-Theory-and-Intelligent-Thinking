'''
Implementation of Binary Tree
Created by: 		Keivan Ipchi Hagh
Creation data:		Monday, November 8, 2020
GitHub:				https://github.com/keivanipchihagh

Purpose of this data structure is to have the minimum possible time complexity for each operation.
Modify the code for your own use.
'''


from typing import Iterator


class Node:
	''' Node object contains a value, a pointers to left and a pointer to the right node '''

	def __init__(self, value):
		''' Construction - Initializes the object variables '''

		self.right = self.left = self.parent = None
		self.value = value


class BinaryTree:
	''' 
	~ Binary Tree (Python 3 edition) ~

	functions:
	- insert					O(long(n))		Return: -			Param: Value 		Contains inline funtion
	- print						O(n)			Return: -			Param: -			Contains inline funtion
	- insert_range				O(n ^ 2)		Return: -			Param: List
	- in_order_traverse			O(n)			Return: -			Param: -			Contains inline funtion
	- pre_order_traverse		O(n)			Return: -			Param: -			Contains inline funtion
	- post_order_traverse		O(n)			Return: -			Param: -			Contains inline funtion
	- exists					O(n)			Return: Boolean		Param: Value
	- get_node					O(log(n))		Return: Node 	 	Param: -
	- get_min					O(log(n))		Return: Min value 	Param: -
	- get_max					O(log(n))		Return: Max value 	Param: -
	- get_successor				O(n)			Return: Successor 	Param: Value
	- get_predecessor			O(n)			Return: Successor 	Param: Value
	- fancy_print				O(n)			Return: -			Param: -			Contains inline funtion
	- delete 					O(n)			Return: -			Param: Value		Contains inline funtion
	'''

	def __init__(self):
		''' Construction - Initializes the object variables to default values '''

		self.root = None
		self.size = 0
		self.min = self.max = None

	def insert(self, value):
		''' Inserts a value to the tree - '''

		def insert(self, value, iterator):
			''' Recursive function to insert new node '''

			if iterator != None:
				if value < iterator.value:

					# Left branch
					if iterator.left is None:						
						iterator.left = Node(value)
						iterator.left.parent = iterator 	# Set parent
					else:
						insert(self, value, iterator.left)
				else:

					# Right branch
					if iterator.right is None:
						iterator.right = Node(value)
						iterator.right.parent = iterator 	# Set parent
					else:
						insert(self, value, iterator.right)
			else:
				self.root = Node(value)		# Tree is empty, craete root node

		iterator = self.root
		insert(self, value, iterator)
		self.size += 1		# Increment size

		# Change minimum
		if self.min is None or value < self.min:
			self.min = value

		# Change maximum
		if self.max is None or value > self.max:
    			self.max = value

	def insert_range(self, ls):
		''' Inserts an iterable to the tree '''

		ls = list(ls)  # Convert to list

		for item in ls:
			self.insert(item)

	def print(self, new_line = True, reversed = False):
		''' Prints the sorted values in the tree - O(n) '''

		def traverse(self, iterator, reversed):
			''' Recursive function to iterate all nodes '''

			# Exigt condition
			if iterator is None:
				return

			traverse(self, iterator.right, reversed) if (reversed == True) else traverse(self, iterator.left, reversed)
			print(iterator.value, end = ' ')
			traverse(self, iterator.left, reversed) if (reversed == True) else traverse(self, iterator.right, reversed)

		# Copy of the root
		iterator = self.root

		# Traverse
		traverse(self, iterator, reversed)

		# Print new line
		if new_line == True:
			print()

	def in_order_traverse(self, new_line = True):
		''' Traverse the list in order '''

		def in_order_traverse(self, iterator):
			''' Recursive in order traverse '''

			# Exit condition
			if iterator is None:
				return

			in_order_traverse(self, iterator.left)
			print(iterator.value, end = ' ')
			in_order_traverse(self, iterator.right)

		iterator = self.root
		in_order_traverse(self, iterator)
		
		# Print new line
		if new_line == True:
			print()

	def pre_order_traverse(self, new_line = True):
		''' Traverse the list pre order '''

		def pre_order_traverse(self, iterator):
			''' Recursive pre order traverse '''

			# Exit condition
			if iterator is None:
    				return

			print(iterator.value, end = ' ')
			pre_order_traverse(self, iterator.left)			
			pre_order_traverse(self, iterator.right)

		iterator = self.root
		pre_order_traverse(self, iterator)
		
		# Print new line
		if new_line == True:
			print()

	def post_order_traverse(self, new_line = True):
		''' Traverse the list post order '''

		def post_order_traverse(self, iterator):
			''' Recursive post order traverse '''

			# Exit condition
			if iterator is None:
    				return
			
			post_order_traverse(self, iterator.left)
			post_order_traverse(self, iterator.right)
			print(iterator.value, end = ' ')

		iterator = self.root
		post_order_traverse(self, iterator)
		
		# Print new line
		if new_line == True:
			print()

	def exists(self, value):
		''' Check whether the given value exists in the tree or not '''

		if self.size == 0: raise Exception('Tree is empty!')

		iterator = self.root
		return True if (self.get_node(value, iterator) == True) else False

	def get_node(self, value, iterator):
		'''  Returns the node containing the given value '''

		# Exit condition
		if iterator is None:
			return iterator

		if value == iterator.value:
			return iterator
		elif value < iterator.value:
			return self.get_node(value, iterator.left)
		else:
			return self.get_node(value, iterator.right)

	def get_min(self, value, get_node = False):
		''' Get the minimum value from a given parent value '''

		iterator = self.root
		iterator = self.get_node(value, iterator)	# Get the corresponding node

		while iterator.left is not None:
			iterator = iterator.left

		return iterator if (get_node == True) else iterator.value

	def get_max(self, value, get_node = False):
		''' Get the maxumum value from a given parent value '''

		iterator = self.root
		iterator = self.get_node(value, iterator)	# Get the corresponding node

		while iterator.right is not None:
			iterator = iterator.right

		return iterator if (get_node == True) else iterator.value

	def get_successor(self, value, get_node = False):
		''' Get the successor for the given value '''

		iterator = self.root
		node = self.get_node(value, iterator)	# Get the corresponding node

		if node.right is not None:
   			return self.get_min(node.right.value)

		parent = node.parent
		while parent is not None and parent.right == node:
			node = parent
			parent = parent.parent	

		return parent if (get_node == True) else parent.value

	def get_predecessor(self, value, get_node = False):
		''' Get the predecessor for the given value '''

		iterator = self.root
		node = self.get_node(value, iterator)	# Get the corresponding node

		if node.left is not None:
			return self.get_max(node.left.value)

		parent = node.parent
		while parent is not None and parent.left == node:
			node = parent
			parent = parent.parent	

		return parent if (get_node == True) else parent.value
  
	def fancy_print(self) : 
		''' Fancy prints the tree '''

		def fancy_print(self, node, space) :
			''' Recursively fancy prints the tree '''

			COUNT = [10]	# Number of spaces

			# Base case  
			if (node == None) : 
				return
 
			# Increase distance between levels  
			space += COUNT[0]
  
			# Process right branch first  
			fancy_print(self, node = node.right, space = space)
  
			# Print current node after space  
			# count  
			print('\n', abs(space - COUNT[0]) * ' ', node.value, sep = '')
	  
			# Process left branch  
			fancy_print(self, node.left, space)    

		temp = self.root
		fancy_print(self, node = temp, space = 0)

	def delete(self, value):
		''' Deletes the given value from the tree 
			Note 3 scenarios:
				1) Node to be deleted is leaf: Simply remove from the tree.
				2) Node to be deleted has only one child: Copy the child to the node and delete the child 
				3) Node to be deleted has two children: Find inorder successor of the node. Copy contents of the inorder successor to the node and delete the inorder successor. Note that inorder predecessor can also be used.
		'''

		def delete(self, node, value):
			''' Recursively search and remove the given value from the tree '''

			# Base caase
			if node is None:
				return node

			# If the given value is smaller than root's value, then it is located in the left brach
			if value < node.value:
				node.left = delete(self, node.left, value)

			# Same applies if the value is on the right branch
			elif value > node.value:
				node.right = delete(self, node.right, value)

			# This is the node we are looking for
			else:

				# Node with one or no child (Scenario 1 & 2)
				if node.left is None:
					temp = node.right
					node = None
					return temp

				elif node.right is None:
					temp = node.left
					node = None
					return temp

				# Node with two children (Scenario 3)
				temp = self.get_min(node.right.value, True)
				node.value = temp.value
				node.right = delete(self, node.right, temp.value)

			return node

		temp = self.root
		delete(self, temp, value)

tree = BinaryTree()													# Initialize

tree.insert(5)														# Push a value

tree.insert_range([3, 7, 6, -1, 2, -2, 1, 12, 10, 14, 8, 11])		# Push an iterable

tree.print(reversed = False)										# Print

#tree.in_order_traverse()

#tree.pre_order_traverse()

#tree.post_order_traverse()

print('Check exists 7:', tree.exists(7))							# Search

print('Mininum value:', tree.min)									# Get minimum value of the entire tree

print('Maximum value after 12:', tree.get_min(12))					# Get the minimum value from the given value

print('Minimum value after 7:', tree.get_max(7))					# Get the maximum value from the given value

print('Successor of 2:', tree.get_successor(2))						# Get the successor for the given value

print('Predecessor of 8:', tree.get_predecessor(8))					# Get the predecessor for the given value

tree.delete(5)

tree.fancy_print()													# Fancy prints the tree