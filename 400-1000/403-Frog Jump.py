class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        dp = [set() for _ in range(len(stones))]
        dp[0].add(1)
        for i in range(0, len(stones) - 1):
            for j in range(i + 1, len(stones)):
                if (stones[j] - stones[i]) in dp[i]:
                    dp[j].add(stones[j] - stones[i])
                    dp[j].add(stones[j] - stones[i] + 1)
                    dp[j].add(stones[j] - stones[i] - 1)
        return len(dp[-1]) != 0
