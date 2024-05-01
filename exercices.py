# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        pointer = head
        if head:
            while pointer.next:
                if pointer.val == pointer.next.val:
                    pointer.next == pointer.next.next
                else:
                    pointer = pointer.next
        return head
    
node5 = ListNode(10)
node4 = ListNode(8, node5)
node3 = ListNode(10, node4)
node2 = ListNode(4, node3)
node1 = ListNode(2, node2)

solution = Solution()
solution.deleteDuplicates(node1)

print(node1)