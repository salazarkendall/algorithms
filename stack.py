class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

  def __str__(self) -> str:
    return f'Node value: {self.value}'

class Stack:
  def __init__(self, value) -> None:
    new_node = Node(value)
    self.top = new_node
    self.height = 1

  def push(self, value):
    new_node = Node(value)
    if self.height == 0:
      self.top = new_node
    else:
      new_node.next = self.top
      self.top = new_node
    self.height += 1

  def pop(self):
    if self.height == 0:
      return None
    temp = self.top
    self.top = self.top.next
    temp.next = None
    self.height -= 1
    return temp

  def __str__(self) -> str:
    result = '['
    temp = self.top
    while temp:
      result += f'{temp.value}'
      temp = temp.next
      if temp:
        result += ', '
    result += ']'
    return result
  
my_stack = Stack(4)
my_stack.push(6)
my_stack.push(8)
my_stack.push(10)
print(my_stack)

my_stack.pop()
my_stack.pop()
print(my_stack)