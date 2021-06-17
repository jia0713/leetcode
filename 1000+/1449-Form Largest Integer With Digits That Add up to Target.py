class Solution(object):
    def largestNumber(self, cost, target):
        """
        :type cost: List[int]
        :type target: int
        :rtype: str
        """
        dp = [-1] * (target + 1)
        dp[0] = 0
        for index, amount in enumerate(cost):
            for j in range(target - amount + 1):
                if dp[j] != -1:
                    dp[j + amount] = max(
                        dp[j + amount], int(str(index + 1) + str(dp[j]))
                    )
        return str(dp[-1]) if dp[-1] != -1 else "0"
