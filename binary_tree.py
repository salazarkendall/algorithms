class Node:
  def __init__(self, value):
    self.value = value
    self.left = self.right = None

  def __str__(self) -> str:
    return f'Node value: {self.value} '

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
    temp = self.root
    while temp:
      if value < temp.value:
        temp = temp.left
      elif value > temp.value:
        temp = temp.right
      else:
        return True
    return False
  
  def __r_contains(self, current_node, value):
    if current_node == None:
      return False
    if current_node.value == value:
      return True
    if value < current_node.value:
      return self.__r_contains(current_node.left, value)
    else:
      return self.__r_contains(current_node.right, value)
    
  def r_contains(self, value):
    return self.__r_contains(self.root, value)
  
  def __r_insert(self, current_node, value):
    if current_node is None:
      return Node(value)
    if value < current_node.value:
      current_node.left = self.__r_insert(current_node.left, value)
    if value > current_node.value:
      current_node.right = self.__r_insert(current_node.right, value)
    return current_node
      
  def r_insert(self, value):
    if self.root == None:
      self.root = Node(value)
    self.__r_insert(self.root, value)
    
  def __delete_node(self, current_node, value):
    if current_node is None:
      return None
    if value < current_node:
      current_node.left = self.__delete_node(current_node.left, value)
    elif value < current_node:
      current_node.right = self.__delete_node(current_node.right, value)
    return current_node

  def delete_node(self, value):
    self.root = self.__delete_node(self.root, value)


