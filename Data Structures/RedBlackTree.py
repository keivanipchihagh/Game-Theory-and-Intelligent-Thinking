'''
Implementation of Red Black Tree
Created by: 		Keivan Ipchi Hagh
Creation data:		Monday, November 8, 2020
GitHub:				https://github.com/keivanipchihagh/Game-Theory-and-Intelligent-Thinking/blob/main/Data%20Structures/RedBlackTree.py
'''

class Node:
	''' Node object contains a value, a pointers to left and a pointer to the right node '''

	def __init__(self, value):
		''' Construction - Initializes the object variables '''

		self.right = self.left = self.parent = self.color = None
		self.value = value

class RedBlackTree:
	''' 
									~ Red Black Tree (Python 3 edition) ~

	Source: https://en.wikipedia.org/wiki/Red%E2%80%93black_tree

	A red–black tree is a kind of self-balancing binary search tree. Each node stores an extra bit representing color, used to ensure that the tree remains approximately balanced during insertions and deletions.
		1. Each node is either red or black.
		2. The root is black. This rule is sometimes omitted. Since the root can always be changed from red to black, but not necessarily vice versa, this rule has little effect on analysis.
		3. All leaves (NIL) are black.
		4. If a node is red, then both its children are black.
		5. Every path from a given node to any of its descendant NIL nodes goes through the same number of black nodes.

	functions:

	- get_parent 				O(1)			Return: Node 		Param: Node
	- get_grand_parent 			O(1)			Return: Node 		Param: Node
	- get_sibling 				O(1)			Return: Node 		Param: Node
	- get_uncle 				O(1)			Return: Node 		Param: Node
	- rotate_left				O(1)			Return: -	 		Param: Node
	- rotate_right				O(1)			Return: -	 		Param: Node
	- insert 					O(log(n)		Return: -	 		Param: Node
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
	- is_subtree*				O(n + m)		Return: Boolean		param: tree

	* Contains inline recursive funtion
	'''

	def __init__(self):
		''' Construction - Initializes the object variables to default values '''

		# Default values
		self.root = None
		self.size = self.height = 0


	def get_parent(self, node):
		''' Returns the node's parent '''

		return None if (node.parent is None) else node.parent


	def get_grand_parent(self, node):
		''' Returns the node's grand parent '''
		
		parent = self.get_parent(node)		
		return self.get_parent(parent)


	def get_sibling(self, node):
		''' Returns the node's sibling ''' 

		# Get node's parent
		parent = self.get_parent(node)

		# Check parent is None
		if parent is None:
			return None

		if parent.left == node:
			return parent.right
		else:
			return parent.left


	def get_uncle(self, node):
		''' Returns the node's uncle '''

		parent = self.get_parent(node)
		return None if (parent is None) else self.get_sibling(parent)


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


	def print(self, new_line = True, reversed = False):
		''' Prints the sorted values in the tree - O(n) '''

		def traverse(self, iterator, reversed):
			''' Recursive function to iterate all nodes '''

			# Exigt condition
			if iterator is None:
				return

			traverse(self, iterator.right, reversed) if (reversed == True) else traverse(self, iterator.left, reversed)
			print(iterator.value, iterator.color, sep = '-', end = ' ')
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
				print(iterator.value, iterator.color, sep = '-', end = ' ')
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
					print(iterator.value, iterator.color, sep = '-', end = ' ')
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
				print(iterator.value, iterator.color, sep = '-', end = ' ')
			array.append(iterator.value)
			pre_order_traverse_recursive(self, iterator.left, array)
			pre_order_traverse_recursive(self, iterator.right, array)

		def pre_order_traverse_none_recursive(self, iterator, array):
			''' Pre Order traverse using stack '''

			stack = []	

			while True:

				if iterator is not None:
					print(iterator.value, iterator.color, sep = '-', end = ' ')
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
				print(iterator.value, iterator.color, sep = '-', end = ' ')
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
					print(last_out.value, iterator.color, sep = '-', end = ' ')
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
			print('\n', abs(space - COUNT[0]) * ' ', node.value + '-' + node.color, sep = '')
	  
			# Process left branch  
			fancy_print(self, node.left, space)    

		temp = self.root
		fancy_print(self, node = temp, space = 0)
		print()


	def rotate_left(self, node):
		''' Rotates the given value to the left '''

		iterator = self.root

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


	def rotate_right(self, node):
		''' Rotates the given node to the right '''

		iterator = self.root

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


	def insert(self, value):

		def insert_recurse(self, iterator, node):
			''' Recursively inserts the new node '''

			if iterator is not None:

				# left branch
				if node.value < iterator.value:					
					if iterator.left is not None:
						insert_recurse(iterator.left, node)		# Go deeper to the left branch
						return
					else:
						iterator.left = node

				# Right branch (Can contain duplicates)
				else:
					if iterator.right is not None:
						insert_recurse(iterator.right, node)	# Go deeper to the right branch
						return
					else:
						iterator.right = node

			node.parent = iterator			# Set parent			
			node.left = node.right = None	# NIL children
			node.color = 'RED'				# Set as 'RED', it violates rules 2 & 3, but it's easy to fix

		def insert_fix(self, node):
			''' Fixex the tree using the 3 cases for insertion '''

			parent = self.get_parent(node)
			uncle = self.get_uncle(node)

			# Case 1
			if parent is None:
				insert_fix_case_1(self, node)

			# Case 2
			elif uncle.color == 'RED':
				insert_fix_case_2(self, node)

			# Case 3 & 4
			elif uncle.color == 'BLACK' and parent.color == 'RED':
				insert_fix_case_3(self, node)

		def insert_fix_case_1(self, node):
			''' In this case, the node is the root. Solution: color it BLACK '''

			# 1. Recolor
			node.color = 'BLACK'
	
		def insert_fix_case_2(self, node):
			''' In this case, the node's uncle and parent are RED. Solution: revert their colors respectively '''

			# 1. Recolor
			self.get_parent(node).color = 'RED'
			self.get_uncle(node).color = 'RED'
			self.get_grand_parent(node).color = 'BLACK'

		def insert_fix_case_3(self, node):
			''' In this case, the node's uncle is BLACK and the error shapes a triangle '''

			parent = self.get_parent(node)
			grand_parent = self.get_grand_parent(node)

			# 1. Rotate
			if node == parent.right and parent == grand_parent.left:
				self.rotate_left(parent)
				node = node.left
			elif node == parent.left and parent == grand_parent.right:
				self.rotate_right(parent)
				node = node.right

			# Now case 4 occures
			insert_fix_case_4(self, node)

		def insert_fix_case_4(self, node):
			''' In this case, the node's uncle us BLACK and the error shapes a line '''

			parent = self.get_parent(node)
			grand_parent = self.get_grand_parent(node)

			# 1. Rotate
			if node == parent.left:
				self.rotate_right(grand_parent)
			else:
				self.rotate_left(grand_parent)

			# 2. Recolor
			parent.color = 'BLACK'
			grand_parent.color = 'RED'		


		iterator = self.root
		node = Node(value)

		# Insert the node to the current tree
		insert_recurse(self, iterator, node)

		# Repair the tree in using the 3 cases if any of the rules are violated
		insert_fix(self, node)


	def insert_range(self, ls):
		''' Inserts a list of items into the tree '''

		for item in ls:
			self.Insert(item)

RB = RedBlackTree()
RB.insert(15)
RB.in_order_traverse()

RB.insert(5)
RB.in_order_traverse()
# RB.fancy_print()