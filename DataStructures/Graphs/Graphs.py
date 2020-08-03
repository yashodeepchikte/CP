class Graph():
    def __init__(self):
        self.adjacencyList = {}
    def addVertex(self, vertex):
        if not(vertex in self.adjacencyList.keys()):
            self.adjacencyList[vertex] = []
        else:
            print("ERROR: ", vertex,   " vertex already exists")
    def addEdge(self, vertex1, vertex2):
        if not(vertex2 in self.adjacencyList[vertex1]):
            self.adjacencyList[vertex1].append(vertex2)
        else:
            print("edge already exisits")
        if not(vertex1 in self.adjacencyList[vertex1]):
            self.adjacencyList[vertex2].append(vertex1)
        else:
            print("edge already exisits")
    def removeEdge(self, vertex1, vertex2):
        self.adjacencyList[vertex1] = list(filter(lambda x: x != vertex2, self.adjacencyList[vertex1]))
        self.adjacencyList[vertex2] = list(filter(lambda x: x != vertex1, self.adjacencyList[vertex2]))
    def removeVertex(self, vertex):
        edges = self.adjacencyList[vertex]
        self.adjacencyList.pop(vertex)
        for edge in edges:
            self.adjacencyList[edge] = list(filter(lambda x: x != vertex, self.adjacencyList[edge]))