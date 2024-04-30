class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

  def __str__(self) -> str:
    return f'Node value: {self.value}'

class LinkedList:
  def __init__(self, value):
    new_node = Node(value)
    self.head = self.tail = new_node
    self.length = 1

  def append(self, value):
    new_node = Node(value)
    self.tail.next = new_node
    self.tail = new_node

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
my_list = LinkedList(0)

for i in range(5):
  my_list.append(i)

print(my_list)