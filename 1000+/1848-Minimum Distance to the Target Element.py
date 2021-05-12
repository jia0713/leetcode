class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        res = float("inf")
        for index, num in enumerate(nums):
            if num == target:
                res = min(res, abs(start - index))
        return res