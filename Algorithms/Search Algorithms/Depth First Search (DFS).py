'''
Implementation of Dooubly linked list
Created by: 		Keivan Ipchi Hagh
Creation data:		Monday, November 2, 2020
GitHub:				https://github.com/keivanipchihagh

Purpose of this data structure is to have the minimum possible time complexity for each operation.
Modify the code for your own use.
'''

class Graph:
	''' Graph class '''

	def __init__(self):
		''' Constructor '''
		self.graph = dict()

	def add_edge(self, edge, nodes):
		''' Adds a new edge to the graph '''

		self.graph[edge] = nodes

	def DFS(self, vertex):
		''' Depth First Search Algortihm - Time complexity: O(V + E) where V is the number of vertices and E is the number of edges in the graph '''

		def DFS(self, vertex, visited):
			''' Recursive PFS algorithm '''

			# Mark vertex as visited
			visited.add(vertex)

			# Print edges value
			print(vertex, end = ' ')

			# Check all adjacent vertecies of the vertex
			for adjacent in self.graph[vertex]:

				if adjacent not in visited:
					DFS(self, adjacent, visited)

		# Create a list to store visited status (Add one extra False for the vertex itself)
		visited = set()

		DFS(self, vertex, visited)
		print()

	def DFS_all(self):
		''' Depth First Search Algortihm - Time complexity: O(V + E) where V is the number of vertices and E is the number of edges in the graph '''

		def DFS(self, vertex, visited):
			''' Recursive PFS algorithm '''

			# Mark vertex as visited
			visited.add(vertex)

			# Print edges value
			print(vertex, end = ' ')

			# Check all adjacent vertecies of the vertex
			for adjacent in self.graph[vertex]:

				if adjacent not in visited:
					DFS(self, adjacent, visited)

		# Create a list to store visited status (Add one extra False for the vertex itself)
		visited = set()

		for vertex in self.graph.keys():
			if vertex not in visited:
				DFS(self, vertex, visited)

		print()




graph = Graph()
graph.add_edge(0, [1, 2])
graph.add_edge(1, [2])
graph.add_edge(2, [0, 3])
graph.add_edge(3, [3])
graph.add_edge(4, [])
# graph.DFS(2)
graph.DFS_all()