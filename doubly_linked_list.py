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

for i in range(10):
  my_doubly_linked_list.append((i+1)*5)

for i in range(20):
  my_doubly_linked_list.pop()


print(my_doubly_linked_list)