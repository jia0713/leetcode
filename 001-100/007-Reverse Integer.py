class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        signal = 1 if x >= 0 else -1
        temp, res = signal * x, 0
        while temp != 0:
            res = 10 * res + temp % 10
            temp = temp // 10
        return res * signal if res <= (2 ** 31) - 1 else 0
