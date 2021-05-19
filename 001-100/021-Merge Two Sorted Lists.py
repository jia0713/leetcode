# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        r, p, q = dummy, l1, l2
        while p and q:
            if p.val <= q.val:
                r.next = ListNode(p.val)
                r, p = r.next, p.next
            else:
                r.next = ListNode(q.val)
                r, q = r.next, q.next
        if p:
            r.next = p
        if q:
            r.next = q
        return dummy.next
