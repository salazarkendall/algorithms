# Definition for singly-linked list.
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists):    
        dummy = ListNode(0)
        pre = dummy
        counter = 0
        no_change = True

        for idx, l in enumerate(lists):
            if l and l.val:
                counter = min(counter, l.val)
            if not l:
                del lists[idx]

        while lists:
            no_change = True
            for idx, l in enumerate(lists):
                current = l
                if l and l.val == counter:
                    l = l.next
                    current.next = None
                    pre.next = current
                    pre = pre.next
                    lists[idx] = l
                    no_change = False
                if not l:
                    del lists[idx]
            if no_change:
                counter+=1
        return dummy.next
    


n1 = ListNode(0)
n2 = ListNode(1)
n3 = ListNode(-2)

s = Solution()
s.mergeKLists([n1,None,n3])