class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_sum = sum(nums)
        if nums_sum % 2 != 0:
            return False
        target = nums_sum // 2
        dp = [False] * (nums_sum + 1)
        dp[0] = True
        for i in range(len(nums)):
            temp_dp = [x for x in dp]
            for j in range(nums_sum):
                if temp_dp[j]:
                    dp[j + nums[i]] = True
            if dp[target]:
                return True
        return False
