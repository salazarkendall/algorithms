class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

  def __str__(self) -> str:
    return f'Node value: {self.value}'
  
class Queue:
  def __init__(self, value) -> None:
    new_node = Node(value)
    self.first = self.last = new_node
    self.length = 1

  def enqueue(self, value):
    new_node = Node(value)
    if self.first is None:
      self.first = self.last = new_node
    else:
      self.last.next = new_node
      self.last = new_node
    self.length += 1
    
  def dequeue(self):
    if self.length == 0:
      return None
    temp = self.first
    if self.length == 1:
      self.first = self.last = None
    else:
      self.first = self.first.next
      temp.next = None
    self.length -= 1
    return temp

  def __str__(self) -> str:
    result = '['
    temp = self.first
    while temp:
      result += f'{temp.value}'
      temp = temp.next
      if temp:
        result += ', '
    result += ']'
    return result

my_queue = Queue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)

print(my_queue)

my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()

print(my_queue)