class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        n_copy = n
        res, cont = 0, 0
        while n > 0:
            n, rest = n // 10, n % 10
            if rest > 1:
                res += 10 ** cont * (n + 1)
            if rest < 1:
                res += 10 ** cont * n
            if rest == 1:
                res += 10 ** cont * n + n_copy % (10 ** cont) + 1
            cont += 1
        return res
