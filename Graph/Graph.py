class graph:

    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

        print("Graph is : ", self.graph_dict)

    def get_paths(self, start, end, path=[]):
        path = path + [start]
        
        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []   
        for node in self.graph_dict[start]:
            if node not in path:
                new_path = self.get_paths(node, end, path)
                for p in new_path:
                    paths.append(p)

        return paths

    def paths(self, start, end):
        if start == end:
            return [start]

        if start not in self.graph_dict:
            return []

        path = [start]

        for p in self.graph_dict[start]:
            new_path = self.paths(p, end)
            for p in new_path:
                path.append(p)

        return path

    def shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start not in self.graph_dict:
            return None

        if start == end:
            return path

        short_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_paths(node, end, path)
                if sp:
                    if short_path is None or len(sp) < len(short_path):
                        short_path = sp       

        return short_path

if __name__ == "__main__":
    path = {
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("New York", "Torento")
    }

    g = graph(path)

    print("Path is : ", g.get_paths("Mumbai", "New York"))
    print("Path is : ", g.paths("Mumbai", "Torento")) 
    print("Path is : ", g.shortest_path("Mumbai", "Dubai")) 