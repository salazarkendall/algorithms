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

    def reverse_between_alternate(self, k: int):

        def check(node, k):
            answer = True
            checker = node
            for _ in range(k):
                if checker is not None:
                    checker = checker.next
                else:
                    answer = False
            return answer

        dummy = Node(0)
        dummy.next = self.head
        pre, current = dummy, self.head

        aux = check(self.head, k)

        while aux:
            pre.next = self.mini_reverse(pre.next, k)
            current = pre.next
            for _ in range(k):
                if pre.next is not None:
                    pre = pre.next
                    current = current.next
                else:
                    current = None
            aux = check(current, k)

        self.head = dummy.next

    def mini_reverse(self, head, amount):
        dummy = Node(0)
        dummy.next = head
        pre = dummy
        current = head
        for _ in range(amount-1):
            after = current.next
            current.next = after.next
            after.next = pre.next
            pre.next = after
        return dummy.next

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

    # TODO: Refactor
    def bubble_sort(self):
        is_sorted = False
        while not is_sorted:
            dummy = Node(0)
            dummy.next = self.head
            pre = dummy
            current = self.head
            is_sorted = True
            while current and current.next:
                if current.value > current.next.value:
                    is_sorted = False
                    after = current.next
                    pre.next = after
                    current.next = after.next
                    after.next = current
                pre = current
                current = current.next
            self.head = dummy.next

    def __selection_sort(self, node: Node):
        if node is None:
            return None
        current = node
        min_node = node
        pre = None
        while current.next:
            if current.next.value < min_node.value:
                min_node = current.next
                pre = current
            current = current.next
        if min_node != node:
            pre.next = min_node.next
            min_node.next = node
        min_node.next = self.__selection_sort(min_node.next)
        return min_node

    def selection_sort(self):
        self.head = self.__selection_sort(self.head)

    # TODO:
    def insertion_sort(self):
        pass


# TESTING
my_list = LinkedList()

my_list.append(4)
my_list.append(2)
my_list.append(1)
my_list.append(6)
my_list.append(5)

# my_list.bubble_sort()
my_list.selection_sort()

print(my_list)
