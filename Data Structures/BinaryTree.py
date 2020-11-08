'''
Implementation of Binary Tree
Created by: 		Keivan Ipchi Hagh
Creation data:		Monday, November 8, 2020
GitHub:				https://github.com/keivanipchihagh

Purpose of this data structure is to have the minimum possible time complexity for each operation.
Modify the code for your own use.
'''


class Node:
	''' Node object contains a value, a pointers to left and a pointer to the right node '''

	def __init__(self, value):
		''' Construction - Initializes the object variables '''

		self.right = self.left = None
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
	- exists					O(n)			Return: Boolean		Param: Value 		Contains inline funtion
	- get_min					O(log(n))		Return: Min value 	Param: - 			Contains inline funtion
	- get_max					O(log(n))		Return: Max value 	Param: - 			Contains inline funtion

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
					else:
						insert(self, value, iterator.left)
				else:

					# Right branch
					if iterator.right is None:
						iterator.right = Node(value)
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
		''' Searches for an spesific value '''

		if self.size == 0: raise Exception('Tree is empty!')

		def search(self, value, iterator):
			''' Recursive search '''

			if iterator is None:
				return False

			if value == iterator.value:
				return True
			elif value < iterator.value:
				return search(self, value, iterator.left)
			else:
				return search(self, value, iterator.right)

		iterator = self.root
		return search(self, value, iterator)








tree = BinaryTree()													# Initialize

tree.insert(5)														# Push a value

tree.insert_range([3, 7, 6, -1, 2, -2, 1, 12, 10, 14, 8, 11])		# Push an iterable

tree.print(reversed = False)										# Print

#tree.in_order_traverse()

#tree.pre_order_traverse()

#tree.post_order_traverse()

print(tree.exists(20))												# Search

print(tree.min)