class MinHeap:
    def __init__(self) -> None:
        self.heap = []

    def __str__(self) -> str:
        return self.heap.__str__()

    def _left_child(self, idx) -> int:
        return (idx * 2) + 1

    def _left_child(self, idx) -> int:
        return (idx * 2) + 2

    def _parent(self, idx) -> int:
        return (idx - 1) // 2

    def _swap(self, idx1, idx2) -> None:
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def insert(self, value) -> None:
        # Add the value to the list
        self.heap.append(value)

        # Set a 'pointer' to this last value
        current = len(self.heap) - 1

        # While:
        #   - The pointer is more than 0
        #   - The current value of the pointer is less than it's parent value
        # Do:
        #   - Swap their values
        #   - Set the pointer to it's parent position
        while current > 0 and self.heap[current] < self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)


min_heap = MinHeap()

min_heap.insert(55)
min_heap.insert(27)
min_heap.insert(18)
min_heap.insert(58)
min_heap.insert(99)
min_heap.insert(72)
min_heap.insert(61)
min_heap.insert(3)

print(min_heap)
