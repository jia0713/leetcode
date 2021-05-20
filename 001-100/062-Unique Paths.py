class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1
        dp = [[1] * m for i in range(n)]
        for j in range(1, n):
            for k in range(1, m):
                dp[j][k] = dp[j - 1][k] + dp[j][k - 1]
        return dp[-1][-1]
