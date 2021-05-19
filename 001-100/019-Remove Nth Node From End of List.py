# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode()
        dummy.next = head
        p, q = dummy, dummy
        for _ in range(n):
            q = q.next
        while q.next != None:
            p = p.next
            q = q.next
        if p.next:
            p.next = p.next.next
        else:
            p.next = None
        return dummy.next
