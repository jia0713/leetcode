class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n % 3 == 2:
            return False
        if n % 3 == 0:
            return self.checkPowersOfThree(n // 3)
        if n % 3 == 1:
            return self.checkPowersOfThree((n - 1) // 3)
