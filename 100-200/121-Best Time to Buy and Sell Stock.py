class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        flag = 0
        for index in range(1, len(prices)):
            if prices[index] < prices[flag]:
                flag = index
            max_profit = max(max_profit, prices[index] - prices[flag])
            index += 1
        return max_profit


# DP solution
class Solution_2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        dp = [0] * len(prices)
        for i in range(1, len(prices)):
            dp[i] = max(0, dp[i - 1]) + (prices[i] - prices[i - 1])
        return max(dp)
