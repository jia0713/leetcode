# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        p, length = head, 1
        while p.next != None:
            length += 1
            p = p.next
        tail = p
        m = k % length
        p = head
        for _ in range(length - m - 1):
            p = p.next
        tail.next = head
        head = p.next
        p.next = None
        return head
