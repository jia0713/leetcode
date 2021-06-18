class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        dp = [[num] for num in nums]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if len(dp[j]) >= len(dp[i]):
                        dp[i] = dp[j] + [nums[i]]
        max_len, res = 0, []
        for item in dp:
            if len(item) > max_len:
                res, max_len = item, len(item)
        return res
