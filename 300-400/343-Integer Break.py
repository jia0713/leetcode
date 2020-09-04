class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n - 1
        a = n // 3
        res = n - a * 3
        if res == 2:
            return 3 ** a * res
        else:
            res += 3
            return 3 ** (a - 1) * res
            