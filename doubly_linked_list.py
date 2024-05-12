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

my_doubly_linked_list = DoublyLinkedList(7)

print(my_doubly_linked_list)