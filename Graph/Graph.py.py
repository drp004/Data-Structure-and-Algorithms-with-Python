from collections import defaultdict

class Graph:
    # Create Graph
    def __init__(self):
        self.graph = defaultdict(list)

    # Add Edges to Graph
    def addEdges(self, u, v):
        self.graph[u].append(v)

    # This Function will give the first path.
    def find_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph.keys():
            return None

        for node in self.graph:
            if node not in path:
                newpath = self.find_path(node, end, path)
                if newpath:
                    return newpath

        return None

    # Print the Graph
    def show_graph(self):
        for node in self.graph:
            print(f"{node} : {self.graph[node]}")

if __name__ == "__main__":
    graph = Graph()

    # Creating the Edges
    graph.addEdges('A', 'B')
    graph.addEdges('A', 'C')
    graph.addEdges('B', 'C')
    graph.addEdges('B', 'D')
    graph.addEdges('C', 'D')
    graph.addEdges('D', 'C')
    graph.addEdges('E', 'F')
    graph.addEdges('F', 'C')

    graph.show_graph()
    
    print(graph.find_path('A', 'D'))