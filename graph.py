class Graph:
  def __init__(self) -> None:
    self.adj_list = {}

  def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

  def add_vertex(self, vertex):
    if vertex not in self.adj_list.keys():
      self.adj_list[vertex] = []
      return True
    return False
  
  def add_edge(self, v1, v2):
    if all(v in self.adj_list for v in (v1, v2)):
      self.adj_list[v1].append(v2)
      self.adj_list[v2].append(v1)
      return True
    return False
  
  def remove_edge(self, v1, v2):
    if all(v in self.adj_list for v in (v1, v2)):
      try:
        self.adj_list[v1].remove(v2)
        self.adj_list[v2].remove(v1)
      except ValueError:
         pass
      return True
    return False
  
  def remove_vertex(self, vertex):
    if vertex in self.adj_list.keys():
      for adj_vertex in self.adj_list[vertex]:
        self.adj_list[adj_vertex].remove(vertex)
      del self.adj_list[vertex]
      return True
    return False
      
  
my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.add_edge('A', 'B')
my_graph.add_edge('A', 'C')
my_graph.add_edge('C', 'D')
my_graph.add_edge('B', 'D')
my_graph.add_edge('A', 'D')

my_graph.print_graph()

my_graph.remove_vertex('D')

my_graph.print_graph()
