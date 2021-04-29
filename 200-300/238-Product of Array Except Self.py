class Solution(object):
    # 此解法未实现constant space
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [1] * len(nums)
        right = [1] * len(nums)
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]
            right[len(nums) - i - 1] = right[len(nums) - i] * nums[len(nums) - i]
        for i in range(len(nums)):
            left[i] = left[i] * right[i]
        return left
