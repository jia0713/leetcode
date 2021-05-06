class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        num.reverse()
        res, cur = [(num[0] + k) % 10], (num[0] + k) // 10
        for i in range(1, len(num)):
            cur = cur + num[i]
            res.append(cur % 10)
            cur = cur // 10
        while(cur != 0):
            res.append(cur % 10)
            cur = cur // 10
        res.reverse()
        return res