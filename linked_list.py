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

  def partition_list(self, x):
    if self.head is None:
      return
    temp = self.head
    aux_1 = Node(0)
    aux_2 = Node(0)
    lower_than = aux_1
    bigger_than = aux_2
    while temp:
      if temp.value < x:
        lower_than.next = temp
        lower_than = temp
      else:
        bigger_than.next = temp
        bigger_than = temp
      temp = temp.next

    lower_than.next = bigger_than.next = None
    lower_than.next = aux_2.next

  def remove_duplicates(self):
    unique_values = set()
    current = self.head
    pre = None
    while current:
      if current.value in unique_values:
        pre.next = current.next
        # self.length -= 1
      else:
        unique_values.add(current.value)
        pre = current
      current = current.next 

  def binary_to_decimal(self):
    current = self.head
    result = 0
    while current:
      result = 2*result + current.value
      current = current.next
    return result

  def reverse_between(self, start_index, end_index):
    if self.length <= 1:
      return
    
    dummy_node = Node(0)
    dummy_node.next = self.head
    previous_node = dummy_node

    for i in range(start_index):
      previous_node = previous_node.next

    current_node = previous_node.next

    for i in range(end_index - start_index):
      node_to_move = current_node.next
      current_node.next = node_to_move.next
      node_to_move.next = previous_node.next
      previous_node.next = node_to_move
    
    self.head = dummy_node.next



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

for i in range(10):
  my_list.append(i)

print(my_list)

my_list.reverse_between(0, my_list.length-1)

print(my_list)