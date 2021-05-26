class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoSums(self, l1, l2):
        l3 = ListNode(0)
        temp = l3
        carry = 0
        while l1 is not None or l2 is not None or carry != 0:
            sum = carry
            if l1 is not None:
                sum += l1.val
                l1 = l1.next
            if l2 is not None:
                sum += l2.val
                l2 = l2.next
            l3.next = ListNode(sum % 10)
            l3 = l3.next
        return temp.next
