class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

  def __str__(self) -> str:
    return f'Node value: {self.value}'

class LinkedList:
  def __init__(self):
    self.head = self.tail = None
    self.length = 0

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

  def insert(self, index, value):
    if index < 0 or index > self.length:
      return False
    if index == 0:
      return self.prepend(value)
    if index == self.length:
      return self.append(value)
    new_node = Node(value)
    pre = self.get_node(index-1)
    new_node.next = pre.next
    pre.next = new_node
    self.length += 1
    return True

  def remove(self, index):
    if index < 0 or index >= self.length:
      return None
    if index == 0:
      return self.shift()
    if index == self.length-1:
      return self.pop()
    pre = self.get_node(index-1)
    temp = pre.next
    pre.next = temp.next
    temp.next = None
    self.length -= 1
    return temp
  
  def reverse(self):
    if self.length == 0:
      return

    temp = self.head
    self.head = self.tail
    self.tail = temp

    before = None
    after = temp.next

    while temp:
      after = temp.next
      temp.next = before
      before = temp
      temp = after

  def find_middle_node(self):
    
    fast = self.head
    slow = self.head

    while fast and fast.next:
      fast = fast.next.next
      slow = slow.next

    return slow

  def has_loop(self):
    slow = fast = self.head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
        return True
    return False

  def find_kth_from_end(self, k):
    if k < 0 or k > self.length:
      return None
    
    slow = fast = self.head

    for _ in range(k):
      fast = fast.next
      if fast is None:
        return None
    
    while fast:
      fast = fast.next
      slow = slow.next
    
    return slow

    
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
  my_list.append(i*10)

print(my_list)

print(my_list.find_kth_from_end(5))