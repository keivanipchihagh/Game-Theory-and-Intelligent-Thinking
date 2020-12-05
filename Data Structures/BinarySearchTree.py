'''
Implementation of Binary Search Tree
Created by: 		Keivan Ipchi Hagh
Creation data:		Monday, November 8, 2020
GitHub:				https://github.com/keivanipchihagh/Game-Theory-and-Intelligent-Thinking/blob/main/Data%20Structures/BinarySearchTree.py
'''

class Node:
	''' Node object contains a value, a pointers to left and a pointer to the right node '''

	def __init__(self, value):
		''' Construction - Initializes the object variables '''

		self.right = self.left = self.parent = None
		self.value = value

class BinarySearchTree:
	''' 
									~ Binary Search Tree (Python 3 edition) ~

	Binary Search Tree (BST), is a specialized form of the Binary Tree where each node has a comparable value. BST has 3 properties which make in sorted:
		1. All keys in left subtree of a key must be smaller	
		2. All keys in right subtree must be greater
		3. By definition has distinct keys and duplicates in binary search tree are not allowed

	functions:
	- insert*					O(long(n))		Return: -			Param: value
	- print						O(n)			Return: -			Param: new_line = True, reversed = False
	- insert_range				O(n.log(n))		Return: -			Param: list
	- in_order_traverse*		O(n)			Return: -			Param: new_line = True
	- pre_order_traverse*		O(n)			Return: -			Param: new_line = True
	- post_order_traverse*		O(n)			Return: -			Param: new_line = True
	- exists					O(n)			Return: Boolean		Param: value
	- get_node					O(log(n))		Return: Node 	 	Param: value, iterator
	- get_min					O(log(n))		Return: Min value 	Param: value, get_node = False
	- get_max					O(log(n))		Return: Max value 	Param: value, get_node = False
	- get_successor				O(n)			Return: Successor 	Param: value, get_node = False
	- get_predecessor			O(n)			Return: Successor 	Param: value, get_node = False
	- fancy_print				O(n)			Return: -			Param: -	
	- delete* 					O(n)			Return: -			Param: value
	- get_depth					O(n)			Return: Depth 		param: value
	- rotate_left				O(n)			Return: -			param: value
	- rotate_right				O(n)			Return: -			param: value
	- is_BST*					O(n)			Return: Boolean		param: -
	- is_subtree*				O(n + m)		Return: Boolean		param: tree

	* Contains inline recursive funtion
	'''

	def __init__(self):
		''' Construction - Initializes the object variables to default values '''

		# Default values
		self.root = None
		self.size = 0
		self.min = self.max = None


	def insert(self, value):
		''' Inserts a value to the tree '''

		def insert(self, value, iterator):
			''' Recursive function to insert a new node to the tree '''

			if iterator != None:
				if value < iterator.value:

					# Left branch (Smaller value)
					if iterator.left is None:						
						iterator.left = Node(value)
						iterator.left.parent = iterator 	# Set parent
					else:
						insert(self, value, iterator.left)
				elif value > iterator.value:

					# Right branch (Greater value)
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

		ls = list(ls)  # Convert to a list

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

		iterator = self.root
		traverse(self, iterator, reversed)

		# Print new line
		if new_line == True:
			print()


	def in_order_traverse(self, new_line = True, no_print = False):
		''' Traverse the list in order '''

		def in_order_traverse_recursive(self, iterator, array):
			''' Recursive in order traverse '''

			# Exit condition
			if iterator is None:
				return

			in_order_traverse_recursive(self, iterator.left, array)

			if no_print == False:
				print(iterator.value, end = ' ')
			array.append(iterator.value)
			in_order_traverse_recursive(self, iterator.right, array)

		def in_order_traverse_none_recursive(self, iterator, array):
			''' In Order traverse using stack '''

			stack = []	

			while True:

				if iterator is not None:
					stack.append(iterator)
					iterator = iterator.left

				# Backtrack the stack
				elif stack:
					iterator = stack.pop()	# Get the last node
					print(iterator.value, end = ' ')
					array.append(iterator.value)
					iterator = iterator.right
				else:
					break

		iterator = self.root
		array = []
		# in_order_traverse_none_recursive(self, iterator, array)
		in_order_traverse_recursive(self, iterator, array)
		
		# Print new line
		if new_line == True:
			print()

		# Returns the array if needed
		return array


	def pre_order_traverse(self, new_line = True, no_print = False):
		''' Traverse the list pre order '''

		def pre_order_traverse_recursive(self, iterator, array):
			''' Recursive pre order traverse '''

			# Exit condition
			if iterator is None:
    				return

			if no_print == False:
				print(iterator.value, end = ' ')
			array.append(iterator.value)
			pre_order_traverse_recursive(self, iterator.left, array)
			pre_order_traverse_recursive(self, iterator.right, array)

		def pre_order_traverse_none_recursive(self, iterator, array):
			''' Pre Order traverse using stack '''

			stack = []	

			while True:

				if iterator is not None:
					print(iterator.value, end = ' ')
					array.append(iterator.value)
					stack.append(iterator)		
					iterator = iterator.left

				# Backtrack the stack
				elif stack:
					iterator = stack.pop()	# Get the last node					
					iterator = iterator.right
				else:
					break

		iterator = self.root
		array = []
		pre_order_traverse_recursive(self, iterator, array)
		#pre_order_traverse_none_recursive(self, iterator, array)

		
		# Print new line
		if new_line == True:
			print()

		# Returns the array if needed
		return array


	def post_order_traverse(self, new_line = True, no_print = False):
		''' Traverse the list post order '''

		def post_order_traverse_recursive(self, iterator, array):
			''' Recursive post order traverse '''

			# Exit condition
			if iterator is None:
    				return
			
			post_order_traverse_recursive(self, iterator.left, array)
			post_order_traverse_recursive(self, iterator.right, array)
			if no_print == False:
				print(iterator.value, end = ' ')
			array.append(iterator.value)

		def post_order_traverse_none_recursive(self, iterator, array):
			''' Pre Order traverse using stack '''

			stack = []
			last_out = None

			if iterator is None:
				return

			while True:
				if iterator is not None:
					stack.append(iterator)
					iterator = iterator.left
					continue
				elif len(stack) == 0:	# Exit condition
					break
				else:
					temp = stack[-1]	# Peek the last node
					if temp.right is not None and temp.right != last_out:
						iterator = temp.right
						continue

					last_out = stack.pop()
					print(last_out.value, end = ' ')
					array.append(iterator.value)

		iterator = self.root
		array = []
		post_order_traverse_recursive(self, iterator, array)
		#post_order_traverse_none_recursive(self, iterator, array)
		
		# Print new line
		if new_line == True:
			print()

		# Returns the array if needed
		return array


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

		# Return node or its value
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

		# Return node or its value
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

		# Return node or its value
		return parent if (get_node == True) else parent.value


	def get_depth(self):
		''' Returns the depth of the tree '''

		def get_depth(self, node):
			''' Recursivly get the depth of the tree '''

			if node is None:
				return -1

			max_left = get_depth(self, node.left)
			max_right = get_depth(self, node.right)

			return max_left + 1 if (max_left > max_right) else max_right + 1

		node = self.root
		return get_depth(self, node)

  
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
		print()


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


	def rotate_left(self, value):
		''' Rotates the given value to the left '''

		iterator = self.root
		node = self.get_node(value, iterator)		# Get the corresponding node for the given value

		# In case value does not exist
		if node is None or node.right is None:
			return

		temp = node.right
		node.right = temp.left

		if temp.left is not None:
			temp.left.parent = node

		temp.parent = node.parent

		if node.parent is None:
			self.root = temp
		elif node is node.parent.left:
			node.parent.left = temp
		else:
			node.parent.right = temp

		temp.left = node
		node.parent = temp			


	def rotate_right(self, value):
		''' Rotates the given value to the right '''

		iterator = self.root
		node = self.get_node(value, iterator)		# Get the corresponding node for the given value

		# In case value does not exist
		if node is None or node.left is None:
			return

		temp = node.left
		node.left = temp.right

		if temp.right is not None:
			temp.right.parent = node

		temp.parent = node.parent

		if node.parent is None:
			self.root = temp
		elif node is node.parent.right:
			node.parent.right = temp
		else:
			node.parent.left = temp

		temp.right = node
		node.parent = temp	


	def is_BST(self, new_line = True):
		''' Traverse the list in order '''

		def is_BST(self, iterator, previous):
			''' Recursive in order traverse '''

			# Exit condition
			if iterator is None:
				return True

			if is_BST(self, iterator.left, previous) == True:
				
				# Check acsending order & duplicate values
				if previous is not None and iterator.value <= previous.value:
					return False			

				# Set previous node
				previous = iterator
				return is_BST(self, iterator.right, previous)		

			return False

		iterator = self.root
		previous = None
		return is_BST(self, iterator, previous)


	def is_subtree(self, tree):
		''' Checks if the given BST tree is the subtree of the current BST tree '''

		def is_subarray(self, arr_1, arr_2):

			i = j = 0

			while i < len(arr_1) and j < len(arr_2):

				if arr_1[i] == arr_2[j]:
					i += 1
					j += 1

					# Second tree traverse completed
					if j == len(arr_2):
						return True

				else:
					i = i - j + 1
					j = 0

			return False

		# Get 'In Order' & 'Pre Order' of tree_1
		tree_1_in_order = self.in_order_traverse()
		tree_1_pre_order = self.pre_order_traverse()

		# Get 'In Order' & 'Pre Order' of tree_2
		tree_2_in_order = tree.in_order_traverse()
		tree_2_pre_order = tree.pre_order_traverse()

		# Compare arrays for each tree respectively
		return is_subarray(self, tree_1_in_order, tree_2_in_order) and is_subarray(self, tree_1_pre_order, tree_2_pre_order)


# tree = BinarySearchTree()											# Initialize

# tree.insert(5)														# Push a value

# tree.insert_range([3, 7, 6, -1, 2, -2, 1, 12, 10, 14, 8, 11, 3])	# Push an iterable

# print(tree.is_BST())

# tree.print(reversed = False)										# Print

# print('In Order Traverse:')
# tree.in_order_traverse()

# print('Pre Order Traverse:')
# print(tree.pre_order_traverse(no_print = True))

# print('Post Order Traverse:')
# tree.post_order_traverse()

# print('Check exists 7:', tree.exists(7))							# Search

# print('Depth:', tree.get_depth())									# Height (Depth)

# print('Mininum value:', tree.min)									# Get minimum value of the entire tree

# print('Maximum value after 12:', tree.get_min(12))					# Get the minimum value from the given value

# print('Minimum value after 7:', tree.get_max(7))					# Get the maximum value from the given value

# print('Successor of 2:', tree.get_successor(2))						# Get the successor for the given value

# print('Predecessor of 8:', tree.get_predecessor(8))					# Get the predecessor for the given value

# tree.delete(5)

# tree.rotate_left(7)

# tree.fancy_print()													# Fancy prints the tree