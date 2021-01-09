'''
Implementation of Depth First Search
Created by: 		Keivan Ipchi Hagh
Creation data:		Monday, November 2, 2020
GitHub:				https://github.com/keivanipchihagh

Purpose of this algorithm is to have the minimum possible time complexity
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

	def depth_first_search(self, vertex, visited):
		''' Recursive PFS algorithm '''

		# Mark vertex as visited
		visited.add(vertex)

		# Print edges value
		print(vertex, end = ' ')

		# Check all adjacent vertecies of the vertex
		for adjacent in self.graph[vertex]:

			if adjacent not in visited:
				self.depth_first_search(adjacent, visited)


	def DFS_connected_graph(self, vertex):
		''' Depth First Search Algortihm for a connected graph - Time complexity: O(V + E) where V is the number of vertices and E is the number of edges in the graph '''

		# Create a list to store visited status (Add one extra False for the vertex itself)
		visited = set()

		self.depth_first_search(vertex, visited)
		print()

	def DFS_disconnected_graph(self, vertex):
		''' Depth First Search Algortihm for a disconnected graph - Time complexity: O(V + E) where V is the number of vertices and E is the number of edges in the graph '''

		# Create a list to store visited status (Add one extra False for the vertex itself)
		visited = set()

		# First run the DSF for the vertex to traverse the connected vertesis
		self.depth_first_search(vertex, visited)

		for vertex in self.graph.keys():
			if vertex not in visited:
				self.depth_first_search(vertex, visited)

		print()




graph = Graph()
graph.add_edge(1, [2, 3])
graph.add_edge(2, [4, 5, 7])
graph.add_edge(3, [6])
graph.add_edge(5, [8])
# graph.DFS_connected_graph(1)
graph.DFS_disconnected_graph(1)