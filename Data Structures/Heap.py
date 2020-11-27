'''
Implementation of Binary Heap
Created by: 		Keivan Ipchi Hagh
Creation data:		Monday, November 27, 2020
GitHub:				https://github.com/keivanipchihagh
'''

class Node:
	''' Node object contains a value, a pointers to left and a pointer to the right node '''

	def __init__(self, value):
		''' Construction - Initializes the object variables '''

		self.right = self.left = self.parent = None
		self.value = value

class BinaryHeap:

	def __init__(self):
		''' Construction - Initializes the object variables to default values '''

		# Default values
		self.root = None
		self.size = 0
		self.min = self.max = None
