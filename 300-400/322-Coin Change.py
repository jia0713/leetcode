class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
        for i in range(1, amount + 1):
            for coin in coins:
                if dp[i] != 1 and coin < i:
                    dp[i] = min(dp[i - coin] + 1, dp[i])
        return dp[-1] if dp[-1] != float("inf") else -1


# 剪枝之后的算法
class Solution_2(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i - coin] + 1, dp[i])
        return dp[-1] if dp[-1] != float("inf") else -1
