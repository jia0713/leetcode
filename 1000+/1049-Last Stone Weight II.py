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


# 0-1背包问题，寻找最接近sum // 2的子集和

class Solution_2(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        target = sum(stones) // 2
        dp = [0] * (target + 1)
        dp[0] = 1
        for stone in stones:
            for i in range(target, stone - 1, -1):
                dp[i] = dp[i] + dp[i - stone]
        for index in range(target, -1, -1):
            if dp[index] != 0:
                return sum(stones) - 2 * index
