class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

  def __str__(self) -> str:
    return f'Node value: {self.value}'

class LinkedList:
  def __init__(self):
    self.head = self.tail = None
    self.length = 1

  def append(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
    self.length += 1
    return True

  def prepend(self, value):
    new_node = Node(value)
    if self.length == 0:
      self.head = self.tail = new_node
    else:
      new_node.next = self.head
      self.head = new_node
    self.length += 1
    return True
    
  def pop(self):
    if self.length == 0:
      return None
    temp = pre = self.head
    while temp.next is not None:
      pre = temp
      temp = temp.next
    self.tail = pre
    self.tail.next = None
    self.length -= 1
    if self.length == 0:
      self.head = self.tail = None
    return temp
  
  def shift(self):
    if self.head is None:
      return None
    temp = self.head
    self.head = temp.next
    temp.next = None
    self.length -= 1
    if self.length == 0:
      self.tail = None
    return temp
  
  def get_node(self, index):
    if index < 0 or index >= self.length:
      return None
    temp = self.head
    for _ in range(index):
      temp = temp.next
    return temp
  
  def set_node(self, index, value):
    temp = self.get_node(index)
    if temp:
      temp.value = value
      return True
    return False

  def __str__(self) -> str:
    result = '['
    temp = self.head
    while temp:
      result += f'{temp.value}'
      temp = temp.next
      if temp:
        result += ', '
    result += ']'
    return result

# TESTING
my_list = LinkedList()

for i in range(5):
  my_list.append(i*2)

print(my_list)

print(my_list.get_node(2))