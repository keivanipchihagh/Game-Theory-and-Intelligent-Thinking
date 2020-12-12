'''
Implementation of Red Black Tree
Created by: 		Keivan Ipchi Hagh
Creation data:		Monday, November 8, 2020
GitHub:				https://github.com/keivanipchihagh/Game-Theory-and-Intelligent-Thinking/blob/main/Data%20Structures/RedBlackTree.py
'''

from BinarySearchTree import BinarySearchTree as BST

class NIL:
	''' NILL '''
    
	def __init__(self, parent = None, value = None):
    
		self.color = 'BLACK'
		self.parent = parent
		self.value = value

class Node:
	''' Node object contains a value, a pointers to left and a pointer to the right node '''

	def __init__(self, value):
		''' Construction - Initializes the object variables '''

		self.right = self.left = NIL()
		self.parent = None
		self.color = 'RED'
		self.value = value


class RedBlackTree(BST):
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
	- insert 					O(log(n)		Return: -	 		Param: value
	- print						O(n)			Return: -			Param: new_line = True, reversed = False
	- insert_range				O(n.log(n))		Return: -			Param: list
	- in_order_traverse*		O(n)			Return: -			Param: new_line = True
	- pre_order_traverse*		O(n)			Return: -			Param: new_line = True
	- post_order_traverse*		O(n)			Return: -			Param: new_line = True
	- fancy_print				O(n)			Return: -			Param: -		
	- delete					O(log(n))		Return: -			Param: value
	- recolor 					O(n)			Return: -			Param: value
	- get_min					O(log(n))		Return: Min value 	Param: value, get_node = False
	- get_max					O(log(n))		Return: Max value 	Param: value, get_node = False
	- get_successor				O(n)			Return: Successor 	Param: value, get_node = False
	- get_predecessor			O(n)			Return: Successor 	Param: value, get_node = False
	- delete 					O(log(n))		Return: -			Raram: value

	functions (Inherited from BST):

	- rotate_left				O(1)			Return: -	 		Param: Node
	- rotate_right				O(1)			Return: -	 		Param: Node			
	- exists					O(n)			Return: Boolean		Param: value
	- get_node					O(log(n))		Return: Node 	 	Param: value, iterator	
	- is_subtree*				O(n + m)		Return: Boolean		param: tree

	* Contains inline recursive funtion
	'''

	def __init__(self):
		''' Construction - Initializes the object variables to default values '''

		super().__init__()

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
		if parent.value is None:
    			return None

		return parent.right if (parent.left == node) else parent.left		


	def get_uncle(self, node):
		''' Returns the node's uncle '''

		parent = self.get_parent(node)
		return None if (parent is None) else self.get_sibling(parent)


	def print(self, new_line = True, reversed = False):
		''' Prints the sorted values in the tree - O(n) '''

		def traverse(self, iterator, reversed):
			''' Recursive function to iterate all nodes '''

			# Exigt condition
			if iterator.value is None:
    				return

			traverse(self, iterator.right, reversed) if (reversed == True) else traverse(self, iterator.left, reversed)
			print(iterator.value, iterator.color[0], sep = '-', end = ' ')
			traverse(self, iterator.left, reversed) if (reversed == True) else traverse(self, iterator.right, reversed)

		iterator = self.root
		traverse(self, iterator, reversed)

		# Print new line
		if new_line == True:
			print()


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


	def get_node(self, value, iterator):
		'''  Returns the node containing the given value '''

		# Exit condition
		if iterator.value is None:
			return iterator

		if value == iterator.value:
			return iterator
		elif value < iterator.value:
			return self.get_node(value, iterator.left)
		else:
			return self.get_node(value, iterator.right)


	def in_order_traverse(self, new_line = True, no_print = False):
		''' Traverse the list in order '''

		def in_order_traverse_recursive(self, iterator, array):
			''' Recursive in order traverse '''

			# Exit condition
			if iterator.value is None:
    				return

			in_order_traverse_recursive(self, iterator.left, array)

			if no_print == False:
				print(iterator.value, iterator.color[0], sep = '-', end = ' ')
			array.append(iterator.value)
			in_order_traverse_recursive(self, iterator.right, array)

		def in_order_traverse_none_recursive(self, iterator, array):
			''' In Order traverse using stack '''

			stack = []	

			while True:

				if iterator.value is not None:
					stack.append(iterator)
					iterator = iterator.left

				# Backtrack the stack
				elif stack:
					iterator = stack.pop()	# Get the last node
					print(iterator.value, iterator.color[0], sep = '-', end = ' ')
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
			if iterator.value is None:
    				return

			if no_print == False:
				print(iterator.value, iterator.color[0], sep = '-', end = ' ')
			array.append(iterator.value)
			pre_order_traverse_recursive(self, iterator.left, array)
			pre_order_traverse_recursive(self, iterator.right, array)

		def pre_order_traverse_none_recursive(self, iterator, array):
			''' Pre Order traverse using stack '''

			stack = []	

			while True:

				if iterator.value is not None:
					print(iterator.value, iterator.color[0], sep = '-', end = ' ')
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
			if iterator.value is None:
    				return
			
			post_order_traverse_recursive(self, iterator.left, array)
			post_order_traverse_recursive(self, iterator.right, array)
			if no_print == False:
				print(iterator.value, iterator.color[0], sep = '-', end = ' ')
			array.append(iterator.value)

		def post_order_traverse_none_recursive(self, iterator, array):
			''' Pre Order traverse using stack '''

			stack = []
			last_out = None

			if iterator.value is None:
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
					print(last_out.value, iterator.color[0], sep = '-', end = ' ')
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


	def get_min(self, value, get_node = False):
		''' Get the minimum value from a given parent value '''

		iterator = self.root
		iterator = self.get_node(value, iterator)	# Get the corresponding node

		while iterator.left.value is not None:
			iterator = iterator.left

		# Return node or its value
		return iterator if (get_node == True) else iterator.value


	def get_max(self, value, get_node = False):
		''' Get the maxumum value from a given parent value '''

		iterator = self.root
		iterator = self.get_node(value, iterator)	# Get the corresponding node

		while iterator.right.value is not None:
			iterator = iterator.right

		return iterator if (get_node == True) else iterator.value


	def get_successor(self, value, get_node = False):
		''' Get the successor for the given value '''

		iterator = self.root
		node = self.get_node(value, iterator)	# Get the corresponding node

		if node.right.value is not None:
   			return self.get_min(node.right.value, get_node)

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

		if node.left.value is not None:
			return self.get_max(node.left.value, get_node)

		parent = node.parent
		while parent is not None and parent.left == node:
			node = parent
			parent = parent.parent	

		# Return node or its value
		return parent if (get_node == True) else parent.value


	def recolor(self, value):
		''' Recolors the given node '''		

		iterator = self.root
		node = self.get_node(value, iterator)
		node.color =  'BLACK' if (node.color == 'RED') else 'RED'


	def exists(self, value):
		''' Check whether the given value exists in the tree or not '''

		if self.size == 0: raise Exception('Tree is empty!')

		iterator = self.root
		return True if (self.get_node(value, iterator) == True) else False
		

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
	
  
	def fancy_print(self, print_NIL = False) : 
		''' Fancy prints the tree '''

		def fancy_print(self, node, space, print_NIL) :
			''' Recursively fancy prints the tree '''

			COUNT = [10]	# Number of spaces

			# Base case
			if (node == None) :
				return
 
			# Increase distance between levels  
			space += COUNT[0]
  
			# Process right branch first  
			if node.value is not None:
				fancy_print(self, node = node.right, space = space, print_NIL = print_NIL)
  
			# Print current node after space 
			if node.value is not None:
				print('\n', abs(space - COUNT[0]) * ' ', str(node.value) + '-' + node.color[0], sep = '')
			elif print_NIL == True:
				print('\n', abs(space - COUNT[0]) * ' ', 'NIL-' + node.color[0], sep = '')
	  
			# Process left branch 
			if node.value is not None:
				fancy_print(self, node = node.left, space = space, print_NIL = print_NIL)    

		temp = self.root
		fancy_print(self, node = temp, space = 0, print_NIL = print_NIL)
		print()	


	def insert(self, value):

		def insert_recurse(self, iterator, node):
			''' Recursively inserts the new node '''

			if iterator.value is not None:
        
				# left branch
				if node.value < iterator.value:					
					if iterator.left.value is not None:
						insert_recurse(self, iterator.left, node)		# Go deeper to the left branch
						return
					else:
						iterator.left = node

				# Right branch (Can contain duplicates)
				else:
					if iterator.right.value is not None:
						insert_recurse(self, iterator.right, node)	# Go deeper to the right branch
						return
					else:
						iterator.right = node

			node.parent = iterator			# Set parent			
			node.left = node.right = NIL()	# NIL children
			node.color = 'RED'				# Set as 'RED', it violates rules 2 & 3, but it's easy to fix

			insert_fix_case_1(self, node)


		def insert_fix_case_1(self, node):
			''' In this case, the node is the root. Solution: color it BLACK '''
 
			# 1. Recolor
			if node.parent.value is None:
    				node.color = 'BLACK'
			else:
				insert_fix_case_1_5(self, node)


		def insert_fix_case_1_5(self, node):
			'''  In this case, the new node has a black parent. All the properties are still satisfied and we return '''
				
			parent = self.get_parent(node)

			if parent.color == 'BLACK':
				return
			else:
				insert_fix_case_2(self, node)


		def insert_fix_case_2(self, node):
			''' In this case, the node's uncle and parent are RED. Solution: revert their colors respectively '''

			uncle = self.get_uncle(node)

			# 1. Recolor
			if uncle.value is not None and uncle.color == 'RED':
				self.get_parent(node).color = 'BLACK'
				self.get_uncle(node).color = 'BLACK'
				self.get_grand_parent(node).color = 'RED'

				insert_fix_case_1(self, self.get_grand_parent(node))		# We might mess up the upper nodes, so recheck recursively
			else:
				insert_fix_case_3(self, node)


		def insert_fix_case_3(self, node):
			''' In this case, the node's uncle is BLACK and the error shapes a triangle '''

			parent = self.get_parent(node)
			grand_parent = self.get_grand_parent(node)

			# 1. Rotate
			if node == parent.right and parent == grand_parent.left:
				self.rotate_left(parent.value)
				node = node.left
			elif node == parent.left and parent == grand_parent.right:
				self.rotate_right(parent.value)
				node = node.right
			
			insert_fix_case_4(self, node)	# We might mess up the upper nodes, so recheck recursively

		def insert_fix_case_4(self, node):
			''' In this case, the node's uncle us BLACK and the error shapes a line '''

			parent = self.get_parent(node)
			grand_parent = self.get_grand_parent(node)

			# 1. Rotate
			if node == parent.left and parent == grand_parent.left:
				self.rotate_right(grand_parent.value)
			else:
				self.rotate_left(grand_parent.value)

			# 2. Recolor
			parent.color = 'BLACK'
			grand_parent.color = 'RED'		


		iterator = self.root
		node = Node(value)

		# In case the root is empty
		if self.root is None:
			self.root = node
			iterator = NIL()

		# Insert the node to the current tree
		insert_recurse(self, iterator, node)

	def insert_range(self, ls):
		''' Inserts a list of items into the tree '''

		for item in ls:
			self.insert(item)


	def delete(self, value):
		''' Deletes the given value from the tree '''

		def delete_case_1(self, node):
			''' Case 1 - No children - Replace the target node with a NIL '''

			# Save node's properties		
			old_node = node

			if node.parent.left == node:
				node.parent.left = NIL(parent = node.parent)
			else:
				node.parent.right = NIL(parent = node.parent)

			# Rule 4 is violated when color is BLACK
			if old_node.color == 'BLACK':
				delete_fixup(node)

		def delete_case_2(self, node, has_left_child):
			''' Case 2 - 1 non-NIL child which is always black - Replace the target node with its only non-NIL child '''

			# Save node's properties
			old_node = node

			# If node is the left child
			if node.parent.left == node:    		
				node.parent.left = node.left if (has_left_child) else node.right
			else:
				node.parent.right = node.left if (has_left_child) else node.right

			if old_node.color == 'BLACK':	# There is NO way the deleted node is RED - So rule 4 is violated (Might as well rule 3)
				delete_fixup(node)

		def delete_case_3(self, node):
			''' Case 3 - 2 non_NIL children - Copy successors value to the target node, then delete the soccessor which leads to either Case 1 or 2 '''

			successor = self.get_successor(value = node.value, get_node = True)

			# Replace node's value with it's successor's
			node.value = successor.value

			# Delete the successor
			delete(self, successor)

		def delete_fixup(self, node):
			''' Fixes any violations in the tree '''
    			

		def delete(self, node):
    
			# Determine children condition
			has_no_child = node.left.value is None and node.right.value is None
			has_left_child = node.left.value is not None and node.right.value is None
			has_right_child = node.left.value is None and node.right.value is not None

			''' Case 1 - No children - Replace the target node with a NIL '''
			if has_no_child:
				delete_case_1(self, node)

			''' Case 2 - 1 non-NIL child which is always black - Replace the target node with its only non-NIL child '''
			if has_right_child or has_left_child:
				delete_case_2(self, node, has_left_child)
   			

			''' Case 3 - 2 non_NIL children - Copy successors value to the target node, then delete the soccessor which leads to either Case 1 or 2 '''
			if not has_no_child:
				delete_case_3(self, node)


		iterator = self.root
		node = self.get_node(value, iterator)		

		# Do nothing when value is not found
		if node is None:
			return;

		# Delete node
		delete(self, node)

# Initialization
RB = RedBlackTree()

# Insert
RB.insert(5)
RB.insert(10)
RB.insert_range([3, 1, 9, 2, 4, 8])
# RB.delete(2)
RB.fancy_print(print_NIL = False)