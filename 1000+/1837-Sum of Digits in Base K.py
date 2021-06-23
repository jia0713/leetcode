class Solution(object):
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        res = 0
        while n > 0:
            n, rest = n // k, n % k
            res += rest
        return res
