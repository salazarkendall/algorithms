class Node:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __str__(self) -> str:
        left = self.left.value if self.left is not None else 'None'
        right = self.right.value if self.right is not None else 'None'
        return f'Value: {self.value}.\n  -Left: {left}\n  -Right: {right}'


class RecursiveTree:
    def __init__(self) -> None:
        self.root = None

    def __contains(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self.__contains(node.left, value)
        if value > node.value:
            return self.__contains(node.right, value)

    def contains(self, value) -> bool:
        return self.__contains(self.root, value)

    def __insert(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self.__insert(node.left, value)
        if value > node.value:
            node.right = self.__insert(node.right, value)
        return node

    def insert(self, value) -> bool:
        if self.root is None:
            self.root = Node(value)
        self.__insert(self.root, value)

    def __delete(self, node, value):
        if node is None:
            return None
        if value < node.value:
            node.left = self.__delete(node.left, value)
        if value > node.value:
            node.right = self.__delete(node.right, value)
        if value == node.value:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:
                sub_tree_min = self.min_value(node.right)
                node.value = sub_tree_min
                node.right = self.__delete(node.right, sub_tree_min)
        return node

    def delete(self, value):
        return self.__delete(self.root, value)

    def min_value(self, node) -> int:
        while node.left is not None:
            node = node.left
        return node.value

    def __balanced_insert(self, num_list):
        if len(num_list) == 1:
            self.insert(num_list[len(num_list)-1])
        else:
            idx = len(num_list)//2
            self.insert(num_list[idx])
            self.__balanced_insert(num_list[:idx])
            self.__balanced_insert(num_list[idx+1:])

    def balanced_insert(self, num_list):
        self.__balanced_insert(num_list)

    def sorted_list_to_bst(self, nums):
        self.root = self.__sorted_list_to_bst(nums, 0, len(nums) - 1)

    def __sorted_list_to_bst(self, nums, left, right):
        if left > right:
            return None

        mid = (left + right) // 2
        current = Node(nums[mid])

        current.left = self.__sorted_list_to_bst(nums, left, mid - 1)
        current.right = self.__sorted_list_to_bst(nums, mid + 1, right)

        return current

    def invert(self):
        self.root = self.__invert_tree(self.root)

    def __invert_tree(self, node):
        if node is None:
            return None
        aux = node.left
        node.left = self.__invert_tree(node.right)
        node.right = self.__invert_tree(aux)
        return node

    def breadth_first_search(self) -> list:
        current = self.root
        queue = []    # <- Node queue
        results = []  # <- Number list
        queue.append(current)
        while len(queue) > 0:
            current = queue.pop(0)
            results.append(current.value)
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        return results

    def bfs_pre_order(self):
        results = []

        def traverse(node):
            results.append(node.value)
            if node.left is not None:
                traverse(node.left)
            if node.right is not None:
                traverse(node.right)
        traverse(self.root)
        return results

    def bfs_post_order(self):
        results = []

        def traverse(node):
            if node.left is not None:
                traverse(node.left)
            if node.right is not None:
                traverse(node.right)
            results.append(node.value)
        traverse(self.root)
        return results

    def bfs_in_order(self):
        results = []

        def traverse(node):
            if node.left is not None:
                traverse(node.left)
            results.append(node.value)
            if node.right is not None:
                traverse(node.right)
        traverse(self.root)
        return results

    def is_valid_bst(self):
        ordered_list = self.bfs_in_order()
        for idx, num in enumerate(ordered_list):
            if idx < len(ordered_list)-1:
                if num > ordered_list[idx+1]:
                    return False
        return True

    def kth_smallest(self, k):
        stack = []
        node = self.root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.value
            node = node.right
        return None


my_tree = RecursiveTree()

my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.kth_smallest(3))

# print(my_tree.is_valid_bst())

# tree = RecursiveTree()
# tree.sorted_list_to_bst([1, 2, 3, 4, 5, 6, 7])

# print(tree.root)
# print(tree.root.left)
# print(tree.root.right)

# print('---INVERT---')
# tree.invert()

# print(tree.root)
# print(tree.root.left)
# print(tree.root.right)

# print('---ANOTHER THREE---')
# another_tree = RecursiveTree()
# another_tree.insert(4)
# another_tree.insert(2)

# print(another_tree.root)
# print('---INVERT---')
# another_tree.invert()
# print(another_tree.root)
