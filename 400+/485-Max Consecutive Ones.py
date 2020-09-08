class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, zero_pos = 0, -1
        for i, num in enumerate(nums):
            if num == 0:
                res = max(res, i - zero_pos - 1)
                zero_pos = i
        if nums[-1] == 1:
            res = max(res, len(nums) - zero_pos - 1)
        return res