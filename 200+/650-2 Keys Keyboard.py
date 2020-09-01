class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 0
        dp = [float("inf")] * (n + 1)
        for i in range(2, n + 1):
            if dp[i] == float("inf"):
                dp[i] = i
            for j in range(2, n // i + 1):
                dp[i * j] = min(dp[i * j], dp[i] + j)
        return dp[-1]