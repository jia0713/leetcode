# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        dummy = ListNode()
        dummy.next = head
        t, p, q = dummy, dummy.next, dummy.next.next
        while p and q:
            t.next = q
            p.next = q.next
            q.next, t = p, p
            p = t.next
            q = p.next if p else None
        return dummy.next
