class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stone_sum = sum(stones)
        dp = [False] * (stone_sum + 1)
        dp[stones[0]] = True
        for i in range(1, len(stones)):
            temp_dp = [x for x in dp]
            dp = [False] * (stone_sum + 1)
            for j in range(len(temp_dp)):
                if temp_dp[j]:
                    dp[j + stones[i]] = True
                    dp[abs(j - stones[i])] = True
        for i in range(len(dp)):
            if dp[i]:
                return i