from collections import Counter


class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = Counter(nums)
        dp = [0] * (max(nums) + 1)
        for index in range(len(dp)):
            dp[index] = counter[index] * index
            if index >= 2:
                dp[index] = max(dp[index] + dp[index - 2], dp[index - 1])
        return dp[-1]
