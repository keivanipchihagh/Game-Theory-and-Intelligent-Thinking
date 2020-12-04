'''
Implementation of MinHeap & MaxHeap
Created by: 		Keivan Ipchi Hagh
Creation data:		Monday, November 8, 2020
GitHub:				https://github.com/keivanipchihagh/Game-Theory-and-Intelligent-Thinking/blob/main/Data%20Structures/Heap.py
'''

class Heap:

	def __init__(self):
		''' Construction - Initializes the object variables to default values '''

		# Default values
		self.root = None
		self.size = 0
		self.array = []	

	def print(self):
		print(' '.join([str(item) for item in self.array]))

class MaxHeap(Heap):

	def __init__(self):
		super(MaxHeap, self).__init__()


	def heapify(self, index):

		largest = index
		left = 2 * index + 1
		right = 2 * index + 2

		if left < self.size and self.array[left] > self.array[largest]:		
			largest = left		

		if right < self.size and self.array[right] > self.array[largest]:
			largest = right

		if largest != index:
			self.array[index], self.array[largest] = self.array[largest], self.array[index]			
			heapify(largest)


	def insert(self, value):
		''' Insert a value into the Heap '''

		# Increment size by one
		self.size += 1

		# Append to the Heap
		self.array.append(value)

		self.heapify(self.size - 1)

maxH = MaxHeap()
maxH.insert(10)
maxH.insert(5)
maxH.insert(3)
maxH.insert(2)
maxH.insert(4)
maxH.insert(15)

maxH.print()