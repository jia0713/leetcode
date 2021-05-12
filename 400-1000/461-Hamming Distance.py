class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        res = 0
        a = x ^ y
        while a != 0:
            res += 1
            a = a & (a - 1)
        return res
