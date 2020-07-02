class Solution:

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        flag = 0
        for index in range(1, len(prices)):
            if (prices[index] < prices[flag]):
                flag = index
            max_profit = max(max_profit, prices[index] - prices[flag])
            index += 1
        return max_profit


if __name__ == "__main__":
    sol = Solution()
    answer = sol.maxProfit([7, 1, 4, 6, 5, 3, 9])
    print (answer)


