'''
Implementation of Breadth First Search
Created by: 		Keivan Ipchi Hagh
Creation data:		Monday, November 2, 2020
GitHub:				https://github.com/keivanipchihagh

Purpose of this algorithm is to have the minimum possible time complexity
Modify the code for your own use.
'''

class Queue:
	''' Queue class '''

	def __init__(self):
		''' Constructor '''

		self.items = []


	def Enqueue(self, item):
		''' Appends an item to the list '''

		self.items.append(item)


	def Dequque(self):
		''' Removes & returns the first item from the list '''

		# Exception handler
		if len(self.items) == 0:
			raise Exception("Queue is empty!")

		item = self.items[0]
		self.items = self.items[1:]

		return item


	def is_empty(self):
		''' Return a boolean indicating whether queue is empty or not '''

		return len(self.items) == 0



class Graph:
	''' Graph class '''

	def __init__(self):
		''' Constructor '''
		self.graph = dict()

	def add_edge(self, edge, nodes):
		''' Adds a new edge to the graph '''

		self.graph[edge] = nodes

	def breadth_first_search(self, vertex, visited):
		''' Recursive PFS algorithm '''

		queue = Queue()

		queue.Enqueue(vertex)	# Add the current vertex to the queue

		visited.add(vertex)		# Add the vertex to the visited list

		while not queue.is_empty():

			item = queue.Dequque()	# Get an item from queue
			print(item, end = ' ')	# Print the item

			for node in self.graph[item]:

				if node not in visited:		# If node has not been previously visited
					visited.add(node)		# Add the node to the visited list

					queue.Enqueue(node)		# Add the node to the queue


	def BFS_connected_graph(self, vertex):
		''' Depth First Search Algortihm - Time complexity: O(V + E) where V is the number of vertices and E is the number of edges in the graph '''

		# Create a list to store visited status (Add one extra False for the vertex itself)
		visited = set()

		self.breadth_first_search(vertex, visited)
		print()

	def BFS_disconnected_graph(self, vertex):
		''' Depth First Search Algortihm - Time complexity: O(V + E) where V is the number of vertices and E is the number of edges in the graph '''		

		# Create a list to store visited status (Add one extra False for the vertex itself)
		visited = set()

		# First run the BSF for the vertex to traverse the connected vertesis
		self.breadth_first_search(vertex, visited)

		for vertex in self.graph.keys():
			if vertex not in visited:
				self.breadth_first_search(vertex, visited)

		print()




graph = Graph()
graph.add_edge(0, [4])
graph.add_edge(1, [2, 3, 4])
graph.add_edge(2, [3])
graph.add_edge(3, [4])
graph.add_edge(4, [])	# Disconnected vertex
# graph.BFS_connected_graph(2)
graph.BFS_disconnected_graph(2)