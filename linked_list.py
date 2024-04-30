class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

  def __str__(self) -> str:
    return f'Node value {self.value}'

class LinkedList:
  def __init__(self, value):
    new_node = Node(value)
    self.head = self.tail = new_node