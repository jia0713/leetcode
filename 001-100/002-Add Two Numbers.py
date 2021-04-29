class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoSums(self, l1, l2):
        l3 = ListNode(0)
        temp = l3
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            sum = carry
            if l1 != None:
                sum += l1.val
                l1 = l1.next
            if l2 != None:
                sum += l2.val
                l2 = l2.next
            l3.next = ListNode(sum % 10)
            l3 = l3.next
        return temp.next


if __name__ == "__main__":

    l1 = [4, 6, 8]
    l2 = [2, 3, 6, 7, 3]
    ans = Solution.addTwoSums(l1, l2)
    print(ans)
