class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        cont, digit = 0, 1
        while cont + 9 * 10 ** (digit - 1) * digit < n:
            cont += 9 * 10 ** (digit - 1) * digit
            digit += 1
        rest = n - cont
        start = 10 ** (digit - 1) - 1
        end = start + rest // digit
        mod = rest % digit
        if mod == 0:
            ans = int(str(end)[-1])
        else:
            ans = int(str(end + 1)[mod - 1])
        return ans
