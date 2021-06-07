# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        pA, pB = headA, headB
        while pA != pB:
            pA, pB = pA.next, pB.next
            if not pA and not pB:
                return None
            if not pA:
                pA = headB
            if not pB:
                pB = headA
        return pA
