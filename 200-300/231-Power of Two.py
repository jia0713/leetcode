class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 注意n=0的情况
        while n % 2 == 0 and n != 0:
            n /= 2
        return n == 1


class Solution_2(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and n & (n - 1) == 0
