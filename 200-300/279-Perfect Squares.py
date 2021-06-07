class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        candis, sqrt = [], int(n ** 0.5)
        for num in range(1, sqrt + 1):
            candis.append(num * num)
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        for candi in candis:
            for i in range(n - candi + 1):
                dp[i + candi] = min(dp[i + candi], dp[i] + 1)
        return dp[-1]
