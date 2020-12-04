'''
Implementation of MinHeap & MaxHeap
Created by: 		Keivan Ipchi Hagh
Creation data:		Monday, November 8, 2020
GitHub:				https://github.com/keivanipchihagh/Game-Theory-and-Intelligent-Thinking/blob/main/Data%20Structures/Heap.py
'''

class MaxHeap:

	def __init__(self):

		# Default values
		self.root = None
		self.size = 0
		self.array = []	


	def heapify(self, index):
		''' Sorts the Heap '''

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

	def insert_range(self, ls):
		''' Inserts a range of items '''

		for item in ls:
			self.insert(item)

	def print(self):
		print(' '.join([str(item) for item in self.array]))

maxH = MaxHeap()
maxH.insert_range([1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17])

maxH.print()