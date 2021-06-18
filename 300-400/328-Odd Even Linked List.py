# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy_odd, dummy_even = ListNode(), ListNode()
        p1, p2, p = dummy_odd, dummy_even, head
        while p:
            p1.next = p
            p, p1 = p.next, p1.next
            if p:
                p2.next = p
                p, p2 = p.next, p2.next
        p2.next = None
        p1.next = dummy_even.next
        return dummy_odd.next
