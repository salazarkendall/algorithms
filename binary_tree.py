class Node:
  def __init__(self, value):
    self.value = value
    self.left = self.rigth = None

  def __str__(self) -> str:
    return f'Node value: {self.value} '

class BinarySearchTree:
  def __init__(self):
    self.root = None