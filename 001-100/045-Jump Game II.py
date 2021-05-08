class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        inf = 1e6
        dp = [inf] * len(nums)
        dp[0] = 0
        if len(nums) == 1:
            return 0
        for index, num in enumerate(nums):
            if index + num >= len(nums) - 1:
                return dp[index] + 1
            for j in range(index + 1, index + num + 1):
                dp[j] = min(dp[j], dp[index] + 1)


# Greedy
class Solution_2(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right, far = 0, 0, 0
        step = 0
        while right < len(nums) - 1:
            while left <= right:
                far = max(far, nums[left] + left)
                left += 1
            right = far
            step += 1
        return step
