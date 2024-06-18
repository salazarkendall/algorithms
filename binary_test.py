class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, value):
    new_node = Node(value)
    if self.root is None:
      self.root = new_node
      return True
    temp = self.root
    while (True):
      if new_node.value == temp.value:
        return False
      if new_node.value < temp.value:
        if temp.left is None:
          temp.left = new_node
          return True
        temp = temp.left
      else:
        if temp.right is None:
          temp.right = new_node
          return True
        temp = temp.right


  def contains(self, value):
    if self.root is None:
      return False
    current_node = self.root
    while True:
      if value == current_node.value:
        return True
      if value < current_node.left:
        current_node = current_node.left
      if value > current_node.right:
        current_node = current_node.right
      if current_node is None:
        return False

tree = BinarySearchTree()
tree.insert(14)
tree.insert(7)
tree.insert(21)

print('Root:', tree.root.value)
print('Left:', tree.root.left.value)
print('Right:', tree.root.right.value)

