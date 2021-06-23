class Solution(object):
    def simplifiedFractions(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for m in range(2, n + 1):
            for k in range(1, m):
                if self.isCoprime(k, m):
                    res.append("{:d}/{:d}".format(k, m))
        return res

    def isCoprime(self, k, m):
        if k == 1 or m == 1:
            return True
        if k > m:
            k, m = m, k
        if m % k == 0:
            return False
        return self.isCoprime(k, m - k)
