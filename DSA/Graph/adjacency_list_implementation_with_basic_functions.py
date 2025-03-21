'''
Graph implementation using an adjacency list representation 
some basic function 
- DFS
- BFS
- PATH EXISTS
'''

class Graph:
    def __init__(self):
        self.graph = {}
    
    # for adding vertex (node)
    def add_vertex(self, vertex):
        if vertex in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, u, v, directed=False):
        if u not in self.graph:
            self.add_vertex(u)
        if v not in self.graph:
            self.add_vertex(v)
        
        self.graph[u].append(v)
        if not directed:
            self.graph[v].append(u)
        
    
    def display(self):
        for vertex, neighbors in self.graph.items():
            print("vertex = ", vertex, " neighbor = ",neighbors)
    
    def bfs(self, start):
        visited = set()
        q = [start]

        while q:
            vertex = q.pop(0)
            if vertex not in visited:
                print("vertex = ", vertex)
                visited.add(vertex)
                for i in self.graph[vertex]:
                    if i not in visited:
                        q.append(i)
        print()


    def dfs(self, start, visited = None):
        if visited is None:
            visited = {}
        
        if start not in visited:
            print(start)
            visited.add(start)
            for i in self.graph[start]:
                self.dfs(i, visited)
        print()


    def path_exist(self, node1, node2):
        if node1 not in self.graph or node2 not in self.graph:
            return False  
        visited = set()
        q = [node1]

        while q:
            vertex = q.pop(0)
            if vertex == node2:
                return True
            if vertex not in visited:
                visited.add(vertex)
                for i in self.graph[vertex]:
                    q.append(i)
        return False