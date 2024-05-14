# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseFirstNodes(head: ListNode, amount: int):
        dummy = ListNode(0, head)
        pre, current = dummy, head
        for _ in range(amount):
            after = current.next
            current.next = after.next
            after.next = pre.next
            pre.next = after
        return dummy.next

    def reverseKGroup(self, head: ListNode, k: int):
        dummy = ListNode(0, head)
        pre, current = dummy, head
        while current:
            pre.next = self.reverseFirstNodes(current, k)
            for _ in range(k):
                pre = pre.next
            current = pre.next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

solution = Solution()
