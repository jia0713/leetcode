class Solution(object):
    def numWays(self, steps, arrLen):
        """
        :type steps: int
        :type arrLen: int
        :rtype: int
        """
        max_range = min(steps // 2 + 2, arrLen + 1)
        dp = [0] * (max_range + 1)
        dp[1] = 1
        mod = 1e9 + 7
        for i in range(steps):
            dp_copy = [item for item in dp]
            for j in range(1, max_range):
                dp[j] = (dp_copy[j - 1] + dp_copy[j + 1] + dp_copy[j]) % mod
        return int(dp[1])
