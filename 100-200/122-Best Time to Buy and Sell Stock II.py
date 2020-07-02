class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sum = 0
        for index in range(1, len(prices)):
            if prices[index] > prices[index - 1]:
                sum = sum + prices[index] - prices[index - 1]
        return sum


if __name__ == "__main__":

    sol = Solution()
    answer = sol.maxProfit([7, 1, 4, 9, 5, 3, 6, 8])
    print (answer)

