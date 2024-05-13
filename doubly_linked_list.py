class Node:
  def __init__(self, value) -> None:
    self.value = value
    self.next = None
    self.prev = None

  def __str__(self) -> str:
    return f'Node value: {self.value}'

class DoublyLinkedList:
  def __init__(self, value) -> None:
    new_node = Node(value)
    self.head = new_node
    self.tail = new_node
    self.length = 1

  def append(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = self.tail = new_node
    else:
      new_node.prev = self.tail
      self.tail.next = new_node
      self.tail = new_node
    self.length += 1
    return True
  
  def pop(self):
    if self.length == 0:
      return None
    temp = self.tail
    if self.length == 1:
      self.head = self.tail = None
    else:
      self.tail = self.tail.prev
      self.tail.next = None
      temp.prev = None
    self.length -= 1
    return temp
  
  def prepend(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = self.tail = new_node
    else:
      self.head.prev = new_node
      new_node.next = self.head
      self.head = new_node
    self.length += 1
    return True

  def shift(self):
    if self.length == 0:
      return None
    temp = self.head
    if self.length == 1:
      self.head = self.tail = None
    else:
      self.head = temp.next
      self.head.prev = None
      temp.next = None
    self.length -= 1
    return temp

  def get_node(self, index):
    if index < 0 or index >= self.length:
      return None
    temp = self.head

    if index < self.length/2:
      for _ in range(index):
        temp = temp.next
    else:
      temp = self.tail
      for _ in range(self.length - 1, index, -1):
        temp = temp.prev
    return temp
  
  def set_node(self, index, value):
    temp = self.get_node(index)
    if temp is not None:
      temp.value = value
      return True
    return False

  def insert(self, index, value):
    if index < 0 or index > self.length:
      return False
    if index == 0:
      return self.prepend(value)
    if index == self.length:
      return self.append(value)
    new_node = Node(value)
    temp = self.get_node(index-1)

    new_node.next = temp.next
    new_node.prev = temp
    temp.next.prev = new_node
    temp.next = new_node
    self.length += 1
    return True
    
  def remove(self, index):
    if index < 0 or index >= self.length:
      return None
    if index == 0:
      return self.shift()
    if index == self.length - 1:
      return self.pop()
    temp = self.get_node(index)
    temp.prev.next = temp.next
    temp.next.prev = temp.prev
    temp.prev = temp.next = None
    self.length -= 1
    return temp

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

my_doubly_linked_list = DoublyLinkedList(0)

my_doubly_linked_list.append(1)
my_doubly_linked_list.append(2)

my_doubly_linked_list.insert(1, 777)

print(my_doubly_linked_list)

my_doubly_linked_list.remove(1)
print(my_doubly_linked_list)