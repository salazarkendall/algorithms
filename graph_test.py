class Graph:
    def __init__(self) -> None:
        self.adj_list = {}

    def __str__(self) -> str:
        resp = ''
        for vertex in self.adj_list:
            resp += f'{vertex}: {self.adj_list[vertex]}\n'
        resp += '------'
        return resp

    def add_vertex(self, vertex) -> bool:
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2) -> bool:
        vertex_exist = v1 in self.adj_list.keys() and v2 in self.adj_list.keys()
        not_already_added = v1 not in self.adj_list[v2] and v2 not in self.adj_list[v1]
        if vertex_exist and not_already_added:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2) -> bool:
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, vertex) -> None:
        if vertex in self.adj_list.keys():
            for ref_vertex in self.adj_list[vertex]:
                self.adj_list[ref_vertex].remove(vertex)
            del self.adj_list[vertex]


# Graph init
my_graph = Graph()

# Add some vertex
my_graph.add_vertex('K')
my_graph.add_vertex('N')
my_graph.add_vertex('D')
my_graph.add_vertex('X')
print(my_graph)

# Add some edges
my_graph.add_edge('K', 'D')
my_graph.add_edge('K', 'N')
my_graph.add_edge('K', 'X')
my_graph.add_edge('N', 'K')
my_graph.add_edge('N', 'X')
my_graph.add_edge('X', 'D')
print(my_graph)

# Remove edges
my_graph.remove_edge('D', 'K')
my_graph.remove_edge('D', 'K')
print(my_graph)

# Remove vertex
my_graph.remove_vertex('K')
my_graph.remove_vertex('K')
print(my_graph)
