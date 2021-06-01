class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, pos, neg = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            temp_pos, temp_neg = pos, neg
            pos = max(temp_pos * nums[i], temp_neg * nums[i], nums[i])
            neg = min(temp_pos * nums[i], temp_neg * nums[i], nums[i])
            res = max(res, pos)
        return res
