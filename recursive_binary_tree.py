class Node:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f'Value: {self.value}.\n  -Left: {self.left}\n  -Right: {self.right}'


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


tree = RecursiveTree()

tree.insert(2)
tree.insert(1)
tree.insert(3)

print(tree.root)
print(tree.root.left)
print(tree.root.right)
