class Node:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f'Value: {self.value}.\n  -Left: {self.left.value if self.left is not None else 'None'}\n  -Right: {self.right.value if self.right is not None else 'None'}'


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

    # def __invert_tree(self, node):
    #     if node is None:
    #         return None
    #     aux = node.left
    #     node.left = node.right
    #     node.right = aux
    #     node.left = self.__invert_tree(node.left)
    #     node.right = self.__invert_tree(node.right)
    #     return node


# tree = RecursiveTree()
# tree.insert(4)
# tree.insert(2)

# print(tree.root)
# tree.invert()
# print(tree.root)


# tree = RecursiveTree()
# tree.balanced_insert([1, 2, 3, 4, 5, 6, 7])

tree2 = RecursiveTree()
tree2.sorted_list_to_bst([1, 2, 3, 4, 5, 6, 7])

print(tree2.root)
print(tree2.root.left)
print(tree2.root.right)

print('---')
tree2.invert()

print(tree2.root)
print(tree2.root.left)
print(tree2.root.right)
