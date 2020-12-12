'''
Implementation of Order Static Tree
Created by: 		Keivan Ipchi Hagh
Creation data:		Monday, November 8, 2020
GitHub:				https://github.com/keivanipchihagh/Game-Theory-and-Intelligent-Thinking/blob/main/Data%20Structures/OrderStaticTree.py
'''

from RedBlackTree import RedBlackTree as RBTree

class Node:
	''' Node object contains a value, a pointers to left and a pointer to the right node '''

	def __init__(self, value):
		''' Construction - Initializes the object variables '''

		self.right = self.left = NIL()
		self.parent = None
		self.color = 'RED'
		self.value = value
		self.size = 0

class OrderStaticTree(RBTree):

	def __init__(self):
		''' Construction - Initializes the object variables to default values '''

		super().__init__()

		# Default values
		self.root = None
		self.size = self.height = 0