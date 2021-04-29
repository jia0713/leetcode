class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_max, current_sum = nums[0], nums[0]
        for j in range(1, len(nums)):
            current_max = max(current_max, current_sum + nums[j], nums[j])
            current_sum = max(nums[j], current_sum + nums[j])
        return current_max
